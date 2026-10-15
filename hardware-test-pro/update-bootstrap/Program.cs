using System;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using System.Drawing;
using System.Reflection;

namespace NaprawaPC.UpdateBootstrap
{
    internal static class Program
    {
        [STAThread]
        private static void Main(string[] args)
        {
            try
            {
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new BootstrapForm());
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    "Nie mozna uruchomic pomocnika aktualizacji:\r\n" + ex,
                    "NAPRAWA PC - Aktualizacja",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            }
        }
    }

    internal sealed class BootstrapForm : Form
    {
        private readonly Label _title;
        private readonly Label _status;
        private readonly Label _details;
        private readonly ProgressBar _progress;
        private readonly PictureBox _artwork;
        private WebClient _client;
        private string _directory;
        private string _tempSetup;
        private string _setupPath;
        private string _logPath;
        private bool _closing;

        public BootstrapForm()
        {
            Text = "NAPRAWA PC - Instalacja aktualizacji " + BuildConfig.AppVersion;
            Width = 620;
            Height = 245;
            MinimumSize = new Size(620, 245);
            MaximumSize = new Size(620, 245);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;
            MinimizeBox = false;
            ShowInTaskbar = true;
            BackColor = Color.FromArgb(7, 17, 31);
            ForeColor = Color.FromArgb(235, 246, 255);
            Font = new Font("Segoe UI", 9F);

            _title = new Label();
            _title.Left = 22;
            _title.Top = 18;
            _title.Width = 455;
            _title.Height = 32;
            _title.Font = new Font("Segoe UI", 12F, FontStyle.Bold);
            _title.ForeColor = Color.FromArgb(45, 196, 255);
            _title.Text = "Aktualizacja NAPRAWA PC HARDWARE TEST PRO";
            Controls.Add(_title);

            _artwork = new PictureBox();
            _artwork.Left = 485;
            _artwork.Top = 8;
            _artwork.Width = 100;
            _artwork.Height = 54;
            _artwork.SizeMode = PictureBoxSizeMode.Zoom;
            _artwork.BackColor = Color.FromArgb(7, 17, 31);
            try
            {
                using (Stream imageStream = Assembly.GetExecutingAssembly().GetManifestResourceStream("DiagnosticArtwork"))
                {
                    if (imageStream != null)
                    {
                        using (Image loaded = Image.FromStream(imageStream))
                            _artwork.Image = new Bitmap(loaded);
                    }
                }
            }
            catch { }
            Controls.Add(_artwork);

            _status = new Label();
            _status.Left = 24;
            _status.Top = 66;
            _status.Width = 560;
            _status.Height = 24;
            _status.Text = "Przygotowywanie instalatora...";
            Controls.Add(_status);

            _progress = new ProgressBar();
            _progress.Left = 24;
            _progress.Top = 95;
            _progress.Width = 560;
            _progress.Height = 24;
            _progress.Minimum = 0;
            _progress.Maximum = 100;
            _progress.Value = 0;
            Controls.Add(_progress);

            _details = new Label();
            _details.Left = 24;
            _details.Top = 132;
            _details.Width = 560;
            _details.Height = 50;
            _details.ForeColor = Color.FromArgb(160, 184, 205);
            _details.Text = "Weryfikacja pliku i instalacja odbywaja sie automatycznie.";
            Controls.Add(_details);

            Shown += delegate { BeginDownload(); };
            FormClosing += OnFormClosing;
        }

        private void BeginDownload()
        {
            try
            {
                Uri uri = new Uri(BuildConfig.SetupUrl);
                if (uri.Scheme != Uri.UriSchemeHttps ||
                    !String.Equals(uri.Host, "github.com", StringComparison.OrdinalIgnoreCase) ||
                    !String.Equals(Path.GetFileName(uri.AbsolutePath), BuildConfig.SetupFilename, StringComparison.OrdinalIgnoreCase))
                    throw new InvalidOperationException("Adres instalatora nie odpowiada zweryfikowanemu plikowi HTTPS GitHub.");

                _directory = Path.Combine(
                    Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                    "NaprawaPC", "Updates");
                Directory.CreateDirectory(_directory);
                _setupPath = Path.Combine(_directory, BuildConfig.SetupFilename);
                _tempSetup = _setupPath + ".bootstrap-download";
                _logPath = Path.Combine(_directory, "installer-" + BuildConfig.AppVersion + ".log");

                if (File.Exists(_setupPath) && IsValidSetup(_setupPath))
                {
                    StartInstall();
                    return;
                }
                try { if (File.Exists(_tempSetup)) File.Delete(_tempSetup); } catch { }

                _status.Text = "Pobieranie pelnego instalatora...";
                _details.Text = "Wersja " + BuildConfig.AppVersion + ". Nie zamykaj tego okna.";
                _progress.Style = ProgressBarStyle.Continuous;
                _client = new WebClient();
                _client.Headers[HttpRequestHeader.UserAgent] = "NAPRAWA-PC-HARDWARE-TEST-PRO-UpdateBootstrap/" + BuildConfig.AppVersion;
                _client.DownloadProgressChanged += OnDownloadProgress;
                _client.DownloadFileCompleted += OnDownloadCompleted;
                _client.DownloadFileAsync(uri, _tempSetup);
            }
            catch (Exception ex)
            {
                ShowFailure("Nie udalo sie przygotowac pobierania instalatora.", ex.ToString());
            }
        }

        private void OnDownloadProgress(object sender, DownloadProgressChangedEventArgs e)
        {
            int p = e.ProgressPercentage;
            if (p < 0) p = 0;
            if (p > 100) p = 100;
            _progress.Value = p;
            _status.Text = "Pobieranie instalatora: " + p + "%";
            _details.Text = FormatBytes(e.BytesReceived) + " / " +
                (e.TotalBytesToReceive > 0 ? FormatBytes(e.TotalBytesToReceive) : "rozmiar nieznany");
        }

        private void OnDownloadCompleted(object sender, AsyncCompletedEventArgs e)
        {
            try
            {
                if (e.Cancelled) throw new IOException("Pobieranie zostalo anulowane.");
                if (e.Error != null) throw e.Error;
                _status.Text = "Weryfikacja SHA-256 i rozmiaru instalatora...";
                _details.Text = "Sprawdzanie podpisanej sumy kontrolnej pobranego pliku.";
                Application.DoEvents();
                if (!IsValidSetup(_tempSetup))
                    throw new InvalidDataException("Rozmiar lub suma SHA-256 instalatora nie zgadza sie z podpisanym manifestem.");

                if (File.Exists(_setupPath)) File.Delete(_setupPath);
                File.Move(_tempSetup, _setupPath);
                _progress.Value = 100;
                StartInstall();
            }
            catch (Exception ex)
            {
                try { if (File.Exists(_tempSetup)) File.Delete(_tempSetup); } catch { }
                ShowFailure("Nie mozna zweryfikowac lub pobrac instalatora.", ex.ToString());
            }
            finally
            {
                if (_client != null)
                {
                    _client.Dispose();
                    _client = null;
                }
            }
        }

        private bool IsValidSetup(string path)
        {
            FileInfo info = new FileInfo(path);
            if (!info.Exists || info.Length != BuildConfig.SetupSize) return false;
            using (FileStream stream = File.OpenRead(path))
            using (SHA256 sha = SHA256.Create())
            {
                string actual = BitConverter.ToString(sha.ComputeHash(stream)).Replace("-", "").ToLowerInvariant();
                if (!String.Equals(actual, BuildConfig.SetupSha256, StringComparison.OrdinalIgnoreCase))
                    return false;
            }
            using (FileStream stream = File.OpenRead(path))
            {
                if (stream.ReadByte() != 0x4D || stream.ReadByte() != 0x5A) return false;
            }
            return true;
        }

        private void StartInstall()
        {
            try
            {
                if (!IsValidSetup(_setupPath))
                    throw new InvalidDataException("Instalator nie przeszedl kontroli rozmiaru, formatu PE i SHA-256.");

                _status.Text = "Uruchamianie instalatora Windows...";
                _details.Text = "Instalator zapisze raport: " + _logPath;
                _progress.Style = ProgressBarStyle.Marquee;

                ThreadPool.QueueUserWorkItem(delegate
                {
                    int exitCode = -1;
                    Exception error = null;
                    try
                    {
                        ProcessStartInfo start = new ProcessStartInfo();
                        start.FileName = _setupPath;
                        start.WorkingDirectory = _directory;
                        start.Arguments = "/SILENT /NORESTART /SP- /LOG=\"" + _logPath + "\"";
                        start.UseShellExecute = true;
                        start.Verb = "runas";
                        using (Process process = Process.Start(start))
                        {
                            if (process == null) throw new InvalidOperationException("Windows nie zwrocil procesu instalatora.");
                            process.WaitForExit();
                            exitCode = process.ExitCode;
                        }
                    }
                    catch (Exception ex) { error = ex; }

                    try
                    {
                        BeginInvoke((MethodInvoker)delegate
                        {
                            _progress.Style = ProgressBarStyle.Continuous;
                            _progress.Value = 100;
                            if (error != null)
                            {
                                ShowFailure("Nie udalo sie uruchomic lub zakonczyc instalacji.", error.ToString());
                            }
                            else if (exitCode != 0)
                            {
                                ShowFailure("Instalator zakonczyl prace z kodem " + exitCode + ".",
                                    "Kod wyjscia: " + exitCode + "\r\nLog: " + _logPath);
                            }
                            else
                            {
                                _status.Text = "Instalacja zakonczona poprawnie.";
                                _details.Text = "Zainstalowano wersje " + BuildConfig.AppVersion + ".";
                                MessageBox.Show(this,
                                    "Aktualizacja " + BuildConfig.AppVersion + " zostala zainstalowana.\r\n\r\n" +
                                    "Raport instalacji: " + _logPath,
                                    "NAPRAWA PC - Aktualizacja zakonczona",
                                    MessageBoxButtons.OK, MessageBoxIcon.Information);
                                _closing = true;
                                Close();
                            }
                        });
                    }
                    catch { }
                });
            }
            catch (Exception ex)
            {
                ShowFailure("Nie mozna uruchomic instalatora.", ex.ToString());
            }
        }

        private void ShowFailure(string headline, string detail)
        {
            _status.Text = headline;
            _status.ForeColor = Color.FromArgb(255, 105, 105);
            _details.Text = "Raport: " + _logPath + "\r\n" + detail;
            MessageBox.Show(this,
                headline + "\r\n\r\n" + detail + (_logPath == null ? "" : "\r\n\r\nFolder aktualizacji: " + _directory),
                "NAPRAWA PC - Blad aktualizacji",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private static string FormatBytes(long bytes)
        {
            if (bytes >= 1024L * 1024L * 1024L) return (bytes / 1024.0 / 1024.0 / 1024.0).ToString("0.00") + " GB";
            if (bytes >= 1024L * 1024L) return (bytes / 1024.0 / 1024.0).ToString("0.0") + " MB";
            return (bytes / 1024.0).ToString("0.0") + " KB";
        }

        private void OnFormClosing(object sender, FormClosingEventArgs e)
        {
            if (!_closing && _client != null && _client.IsBusy)
            {
                e.Cancel = true;
                MessageBox.Show(this, "Pobieranie aktualizacji trwa. Nie zamykaj okna.", "NAPRAWA PC",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}
