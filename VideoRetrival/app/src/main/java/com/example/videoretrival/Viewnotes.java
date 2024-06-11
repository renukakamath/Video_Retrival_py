package com.example.videoretrival;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Viewnotes extends AppCompatActivity implements JsonResponse {

    ListView l1;
    SharedPreferences sh;
    String[] fname,subject,value,notes,date,statu;
    public static String amt,vid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewnotes);
        l1=(ListView) findViewById(R.id.list);
//        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Viewnotes.this;
        String q = "/Viewnotes?log_id=" +sh.getString("log_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);

    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                fname = new String[ja1.length()];
                subject = new String[ja1.length()];
                value = new String[ja1.length()];
                notes = new String[ja1.length()];
                date = new String[ja1.length()];
                statu = new String[ja1.length()];



                value = new String[ja1.length()];



                String[] value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    fname[i] = ja1.getJSONObject(i).getString("fname");

                    notes[i] = ja1.getJSONObject(i).getString("notes");
                    subject[i] = ja1.getJSONObject(i).getString("subject");

                    date[i] = ja1.getJSONObject(i).getString("date");


                    statu[i] = ja1.getJSONObject(i).getString("status");



                    value[i] = "teacher name:" + fname[i]  +"\n subject:" + subject[i]  +"\n notes:" + notes[i]  +"\n date:" + date[i]  +"\nstatus:" + statu[i]  ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);

            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }
}