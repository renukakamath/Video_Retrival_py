package com.example.videoretrival;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Searchkeyword extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {

    EditText e1;
    ListView l1;
    String[] frames,farme_id,keyword,value,keyword_id,video_id;
    String search,status;
    public static String sid,vid;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_searchkeyword);
        e1=(EditText)findViewById(R.id.search);
        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Searchkeyword.this;
        String q = "/viewSearchkeyword";
        q = q.replace(" ", "%20");
        JR.execute(q);

        e1.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void afterTextChanged(Editable editable) {

                search=e1.getText().toString();

                JsonReq JR = new JsonReq();
                JR.json_response = (JsonResponse) Searchkeyword.this;
                String q = "/Searchkeyword?&search=" + search ;
                q = q.replace(" ", "%20");
                JR.execute(q);

            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {


            status = jo.getString("status");
            Log.d("pearlssssss", status);


            if (status.equalsIgnoreCase("success")) {
                l1.setVisibility(View.VISIBLE);
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                frames = new String[ja1.length()];
                farme_id = new String[ja1.length()];
                keyword = new String[ja1.length()];
                value = new String[ja1.length()];
                keyword_id = new String[ja1.length()];
                video_id = new String[ja1.length()];





                value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    frames[i] = ja1.getJSONObject(i).getString("frames");
                    farme_id[i] = ja1.getJSONObject(i).getString("farme_id");
                    keyword[i] = ja1.getJSONObject(i).getString("keyword");
                    keyword_id[i] = ja1.getJSONObject(i).getString("keyword_id");
                    video_id[i] = ja1.getJSONObject(i).getString("video_id");


                    value[i] = "\nframes:" + frames[i] +"\nkeyword:"+ keyword[i] ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);



            }
            else{
                Toast.makeText(getApplicationContext(),"No Data",Toast.LENGTH_LONG).show();
                l1.setVisibility(View.GONE);
            }



        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        vid=video_id[i];
        final CharSequence[] items = {"View Video","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(Searchkeyword.this);
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("View Video")) {


                    startActivity(new Intent(getApplicationContext(), Videos.class));


                }  else if (items[item].equals("Cancel")) {


                    dialog.dismiss();
                }



            }

        });
        builder.show();
    }
}