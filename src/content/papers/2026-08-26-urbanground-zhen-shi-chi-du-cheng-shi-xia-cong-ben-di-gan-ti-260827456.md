---
title: 'UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City'
title_zh: UrbanGround：真实尺度城市下从本地感知到空间智能体的评测沙箱
authors:
- Tianjie Ju
- Zheng Wu
- Yueqing Sun
- Yuhan Cui
- Bobo Li
- Shengqiong Wu
- Pengzhou Cheng
- Haodong Zhao
- Zongru Wu
- Xinbei Ma
affiliations:
- Shanghai Jiao Tong University
- National University of Singapore
- Meituan
- The Chinese University of Hong Kong
- University of Oxford
arxiv_id: '2608.27456'
url: https://arxiv.org/abs/2608.27456
pdf_url: https://arxiv.org/pdf/2608.27456
published: '2026-08-26'
collected: '2026-08-29'
category: Agent
direction: MLLM智能体 · 真实城市空间能力评测
tags:
- MLLM
- Embodied Agent
- Spatial Reasoning
- Navigation
- Evaluation Sandbox
one_liner: 构建首个基于香港全量3D地理数据的真实城市沙箱，评测MLLM智能体的空间感知与行动能力
practical_value: '- 做本地生活到店、即时配送场景的Agent导航能力评测时，可参考该沙箱的真实3D空间建模、第一人称交互闭环设计，降低模拟与真实场景的gap

  - 评估多模态Agent长序列任务表现时，可复用三层评测框架：本地场景grounding→长距离导航→动态环境鲁棒性，分层拆解能力短板

  - 开发户外AR导购、城市营销类多模态Agent时，可优先优化方向感知、行人动态避让、长路径错误累积修正三类核心短板'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM可解读街景输入，但无法验证其移动过程中本地感知能力是否能支撑真实城市场景下的连续智能行动，此前无对应高保真评测环境。
### 方法关键点
1. 构建UrbanGround沙箱：基于香港全量3D地理数据还原带物理约束的真实城市，支持第一人称闭环交互、交互式导航地图，兼容程序控制的MLLM Agent直接接入；
2. 设计三层递进评测范式：先测主动观察后的本地场景空间问答能力，再测不同距离/目的地模糊度的导航能力，最后测路径变动、行人动态场景下的行动鲁棒性。
### 关键结果
当前主流MLLM Agent仅在视觉识别、短距离空间推理等原子能力上表现可用，方向感知、行人感知移动能力可靠性不足；长距离探索时局部能力无法组合为持续的目标导向行为，错误累积后无有效校正机制，整体长程空间任务表现较差。
