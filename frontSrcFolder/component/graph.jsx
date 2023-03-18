import { ResponsiveLine } from '@nivo/line';
import './graph.css'
export const MyResponsiveLine = ({ data /* see data tab */ }) => (
  <ResponsiveLine
    data={data}
    margin={{ top: 70, right: 110, bottom: 50, left: 60 }}
    xScale={{ type: 'point' }}
    yScale={{
      type: 'linear',
      min: 'auto',
      max: 'auto',
      stacked: true,
      reverse: false
    }}
    yFormat=" >-.2f"
    axisTop={{
      orient: 'top',
      tickSize: 5,
      tickPadding: 5,
      tickRotation: 0,
      legend: '일일 활동',
      legendOffset: -50,
      legendPosition: 'middle',
      tickdata: {
        fontSize: 20 // 원하는 폰트 크기로 변경
      }
    }}
    axisRight={null}
    axisBottom={null}
    axisLeft={{
      orient: 'left',
      tickSize: 5,
      tickPadding: 5,
      tickRotation: 0,
      legend: 'count',
      legendOffset: -40,
      legendPosition: 'middle'
    }}
    pointSize={10}
    pointColor={{ theme: 'background' }}
    pointBorderWidth={2}
    pointBorderColor={{ from: 'serieColor' }}
    pointdataYOffset={-12}
    useMesh={true}
    legends={[
      {
        anchor: 'bottom-right',
        direction: 'column',
        justify: false,
        translateX: 100,
        translateY: 0,
        itemsSpacing: 0,
        itemDirection: 'left-to-right',
        itemWidth: 80,
        itemHeight: 20,
        itemOpacity: 0.75,
        symbolSize: 12,
        symbolShape: 'circle',
        symbolBorderColor: 'rgba(0, 0, 0, .5)',
        effects: [
          {
            on: 'hover',
            style: {
              itemBackground: 'rgba(0, 0, 0, .03)',
              itemOpacity: 1
            }
          }
        ]
      }
    ]}
  />
)

export const d=[
    {
      "id": "japan",
      "color": "hsl(320, 70%, 50%)",
      "data": [
        {
          "x": "plane",
          "y": 273
        },
        {
          "x": "helicopter",
          "y": 47
        },
        {
          "x": "boat",
          "y": 201
        },
        {
          "x": "train",
          "y": 287
        },
        {
          "x": "subway",
          "y": 140
        },
        {
          "x": "bus",
          "y": 90
        },
        {
          "x": "car",
          "y": 90
        },
        {
          "x": "moto",
          "y": 43
        },
        {
          "x": "bicycle",
          "y": 65
        },
        {
          "x": "horse",
          "y": 90
        },
        {
          "x": "skateboard",
          "y": 152
        },
        {
          "x": "others",
          "y": 6
        }
      ]
    },
]

export const petData = [
  {
    keys: 'day',
    label:'하루',
    data: [
      {
        id: '그루밍',
        data: [
          {
            x: '00',
            y: 600,
          },
          {
            x: '01',
            y: 300,
          },
          {
            x: '02',
            y: 350,
          },
          {
            x: '03',
            y: 450,
          },
          {
            x: '04',
            y: 50,
          },
          {
            x: '05',
            y: 550,
          },
          {
            x: '06',
            y: 6,
          },
          {
            x: '07',
            y: 600,
          },
          {
            x: '08',
            y: 600,
          },
          {
            x: '09',
            y: 600,
          },
          {
            x: '10',
            y: 600,
          },
          {
            x: '11',
            y: 600,
          },
          {
            x: '12',
            y: 60,
          },
          {
            x: '13',
            y: 600,
          },
          {
            x: '14',
            y: 600,
          },
          {
            x: '15',
            y: 600,
          },
          {
            x: '16',
            y: 60,
          },
          {
            x: '17',
            y: 600,
          },
          {
            x: '18',
            y: 600,
          },
          {
            x: '19',
            y: 600,
          },
          {
            x: '20',
            y: 600,
          },
          {
            x: '21',
            y: 600,
          },
          {
            x: '22',
            y: 600,
          },
          {
            x: '23',
            y: 600,
          },
        ],
      },
      {
        id: '걷기',
        data: [
          {
            x: '00',
            y: 60,
          },
          {
            x: '01',
            y: 30,
          },
          {
            x: '02',
            y: 50,
          },
          {
            x: '03',
            y: 40,
          },
          {
            x: '04',
            y: 50,
          },
          {
            x: '05',
            y: 50,
          },
          {
            x: '06',
            y: 60,
          },
          {
            x: '07',
            y: 60,
          },
          {
            x: '08',
            y: 60,
          },
          {
            x: '09',
            y: 600,
          },
          {
            x: '10',
            y: 200,
          },
          {
            x: '11',
            y: 660,
          },
          {
            x: '12',
            y: 300,
          },
          {
            x: '13',
            y: 600,
          },
          {
            x: '14',
            y: 600,
          },
          {
            x: '15',
            y: 600,
          },
          {
            x: '16',
            y: 600,
          },
          {
            x: '17',
            y: 600,
          },
          {
            x: '18',
            y: 600,
          },
          {
            x: '19',
            y: 600,
          },
          {
            x: '20',
            y: 600,
          },
          {
            x: '21',
            y: 600,
          },
          {
            x: '22',
            y: 600,
          },
          {
            x: '23',
            y: 600,
          },
        ],
      }
    ]
  },
  {
    keys: 'week',
    label: '한 주',
    data: [
      {

        id: '그루밍',
        data: [
          {
            x: '00',
            y: 600,
          },
          {
            x: '01',
            y: 300,
          },
          {
            x: '02',
            y: 350,
          },
          {
            x: '03',
            y: 450,
          },
          {
            x: '04',
            y: 500,
          },
          {
            x: '05',
            y: 550,
          },
          {
            x: '06',
            y: 600,
          },
          {
            x: '07',
            y: 600,
          },
          {
            x: '08',
            y: 600,
          },
          {
            x: '09',
            y: 600,
          },
          {
            x: '10',
            y: 600,
          },
          {
            x: '11',
            y: 600,
          },
          {
            x: '12',
            y: 600,
          },
          {
            x: '13',
            y: 600,
          },
          {
            x: '14',
            y: 600,
          },
          {
            x: '15',
            y: 600,
          },
          {
            x: '16',
            y: 600,
          },
          {
            x: '17',
            y: 600,
          },
          {
            x: '18',
            y: 600,
          },
          {
            x: '19',
            y: 600,
          },
          {
            x: '20',
            y: 600,
          },
          {
            x: '21',
            y: 600,
          },
          {
            x: '22',
            y: 600,
          },
          {
            x: '23',
            y: 600,
          },
        ],
      },
      {
        id: '걷기',
        data: [
          {
            x: '00',
            y: 60,
          },
          {
            x: '01',
            y: 30,
          },
          {
            x: '02',
            y: 50,
          },
          {
            x: '03',
            y: 40,
          },
          {
            x: '04',
            y: 50,
          },
          {
            x: '05',
            y: 50,
          },
          {
            x: '06',
            y: 60,
          },
          {
            x: '07',
            y: 60,
          },
          {
            x: '08',
            y: 60,
          },
          {
            x: '09',
            y: 600,
          },
          {
            x: '10',
            y: 200,
          },
          {
            x: '11',
            y: 660,
          },
          {
            x: '12',
            y: 300,
          },
          {
            x: '13',
            y: 600,
          },
          {
            x: '14',
            y: 600,
          },
          {
            x: '15',
            y: 600,
          },
          {
            x: '16',
            y: 600,
          },
          {
            x: '17',
            y: 600,
          },
          {
            x: '18',
            y: 600,
          },
          {
            x: '19',
            y: 600,
          },
          {
            x: '20',
            y: 600,
          },
          {
            x: '21',
            y: 600,
          },
          {
            x: '22',
            y: 600,
          },
          {
            x: '23',
            y: 600,
          },
        ],
      }
    ]
  },
  {
    keys: 'month',
    label: '한 달',
    data: [
      {

        id: '그루밍',
        data: [
          {
            x: '00',
            y: 600,
          },
          {
            x: '01',
            y: 300,
          },
          {
            x: '02',
            y: 350,
          },
          {
            x: '03',
            y: 450,
          },
          {
            x: '04',
            y: 500,
          },
          {
            x: '05',
            y: 550,
          },
          {
            x: '06',
            y: 600,
          },
          {
            x: '07',
            y: 600,
          },
          {
            x: '08',
            y: 600,
          },
          {
            x: '09',
            y: 600,
          },
          {
            x: '10',
            y: 600,
          },
          {
            x: '11',
            y: 600,
          },
          {
            x: '12',
            y: 600,
          },
          {
            x: '13',
            y: 600,
          },
          {
            x: '14',
            y: 600,
          },
          {
            x: '15',
            y: 600,
          },
          {
            x: '16',
            y: 600,
          },
          {
            x: '17',
            y: 600,
          },
          {
            x: '18',
            y: 600,
          },
          {
            x: '19',
            y: 600,
          },
          {
            x: '20',
            y: 600,
          },
          {
            x: '21',
            y: 600,
          },
          {
            x: '22',
            y: 600,
          },
          {
            x: '23',
            y: 600,
          },
        ],
      },
      {
        id: '걷기',
        data: [
          {
            x: '00',
            y: 60,
          },
          {
            x: '01',
            y: 30,
          },
          {
            x: '02',
            y: 50,
          },
          {
            x: '03',
            y: 40,
          },
          {
            x: '04',
            y: 50,
          },
          {
            x: '05',
            y: 50,
          },
          {
            x: '06',
            y: 60,
          },
          {
            x: '07',
            y: 60,
          },
          {
            x: '08',
            y: 60,
          },
          {
            x: '09',
            y: 600,
          },
          {
            x: '10',
            y: 200,
          },
          {
            x: '11',
            y: 660,
          },
          {
            x: '12',
            y: 300,
          },
          {
            x: '13',
            y: 600,
          },
          {
            x: '14',
            y: 600,
          },
          {
            x: '15',
            y: 600,
          },
          {
            x: '16',
            y: 600,
          },
          {
            x: '17',
            y: 600,
          },
          {
            x: '18',
            y: 600,
          },
          {
            x: '19',
            y: 600,
          },
          {
            x: '20',
            y: 600,
          },
          {
            x: '21',
            y: 600,
          },
          {
            x: '22',
            y: 600,
          },
          {
            x: '23',
            y: 600,
          },
        ],
      }
    ]
  }
];