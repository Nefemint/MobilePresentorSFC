package com.example.mobilepresentorsfc;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {
    private String code;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Intent intent = getIntent();
        code = intent.getStringExtra("code");
        String[] fingerprints = VKUtil.getCertificateFingerprint(this, this.getPackageName());
        System.out.println(Arrays.asList(fingerprints));
        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.WRITE_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(this,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE)) {
            } else {
                ActivityCompat.requestPermissions(this,
                        new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 1);
            }
        } else {
            // Permission has already been granted
        }
    }

    public void onVKClick(View view) {
        Intent vkIntent = new Intent(this, VKLoginActivity.class);
        vkIntent.putExtra("code", code);
        startActivity(vkIntent);
    }

    public void onGoogleClick(View view) {
        Intent googleDriveIntent = new Intent(this, GoogleDriveLoginActivity.class);
        googleDriveIntent.putExtra("code", code);
        startActivity(googleDriveIntent);
    }
}
