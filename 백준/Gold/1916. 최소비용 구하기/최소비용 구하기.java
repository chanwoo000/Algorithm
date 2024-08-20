import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
    int V, E;
    public Node(int V, int E){
        this.V = V;
        this.E = E;
    }
    @Override
    public int compareTo(Node o) {
        return E - o.E;
    }
}
public class Main{
    static ArrayList<Node> list[];
    static int dist[];
    static boolean visit[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());

        dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        list = new ArrayList[N + 1];
        visit = new boolean[N + 1];

        for(int i=0; i<=N; i++){
            list[i] = new ArrayList<>();
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            list[start].add(new Node(end, num));
        }

        st = new StringTokenizer(br.readLine());
        int go = Integer.parseInt(st.nextToken());
        int finish = Integer.parseInt(st.nextToken());


        PriorityQueue<Node> chanwoo = new PriorityQueue<>();
        chanwoo.offer(new Node(go, 0));
        dist[go] = 0;

        while(!chanwoo.isEmpty()){
            Node poll = chanwoo.poll();
            if(!visit[poll.V]) {
                visit[poll.V] = true;
                for(int i=0; i< list[poll.V].size(); i++) {
                    Node node = list[poll.V].get(i);
                    if(dist[node.V] > poll.E + node.E){
                        dist[node.V] = node.E + poll.E;
                        chanwoo.add(new Node(node.V,dist[node.V]));
                    }
                }
            }
        }

        System.out.println(dist[finish]);
    }
}