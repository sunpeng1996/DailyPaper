---
title: 'Seek to Segment: Active Perception for Panoramic Referring Segmentation'
title_zh: 主动全景指代分割：面向360°环境的具身Agent感知方法
authors:
- Song Tang
- Shuming Hu
- Xincheng Shuai
- Henghui Ding
- Yu-Gang Jiang
affiliations:
- Fudan University
arxiv_id: '2607.02497'
url: https://arxiv.org/abs/2607.02497
pdf_url: https://arxiv.org/pdf/2607.02497
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: 具身Agent · 主动视觉感知
tags:
- Embodied AI
- VLM
- Agent Memory
- Active Perception
- Referring Segmentation
one_liner: 提出主动全景指代分割任务与空间记忆增强的PanoSeeker Agent，性能显著优于适配的SOTA基线
practical_value: '- 可复用EgoSphere固定分辨率空间记忆设计，落地线下门店导航Agent、全景逛店商品查找场景，无需存储历史对话/观测帧，大幅降低冗余探索和算力开销

  - 可迁移「专家轨迹SFT预训练 + GRPO RL优化效率」的训练范式，适配所有需要路径规划的Agent任务，相较直接RL收敛速度更快、探索效率更高

  - 可直接复用APRS的四类空间指代表达分类体系（EGO/UNIQ/ALLO/MULTIHOP），构建全景逛店、虚拟看房场景的用户query标注规范，提升多轮交互匹配准确率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有指代分割模型被动处理固定视角静态图像，无法适配具身AI场景下360°连续环境的主动探索需求；传统3D重建方案算力成本过高，直接处理平铺全景图存在严重几何畸变，分割视角序列又会丢失全局空间上下文，存在明显技术落地瓶颈。

### 方法关键点
- 提出全新任务APRS：要求Agent根据用户语言指令，主动调整视角在360°环境中搜索目标并输出分割掩码
- 设计EgoSphere空间视觉记忆：将顺序局部观测通过逆球心投影逐帧拼接为固定分辨率360°等距柱状全景图，叠加十字准星、经纬网格、历史轨迹提示，保持全局空间一致性，避免冗余探索
- 训练范式：先在专家标注的搜索轨迹数据集上做SFT，再用GRPO强化学习优化探索效率；找到目标后主动对齐视角，调用SAM-3输出高精度分割掩码

### 关键实验结果
在自建的7420样本APRS基准上测试，对比三类基线：静态RIS方法、启发式扫描方法、基于文本日志记忆的VLM Agent。PanoSeeker实现75.4% SR、55.8% mIoU，SPL达0.57，较GPT-5.2基线SPL提升58%，平均搜索步长仅4.8步。

### 核心洞见
对需要空间推理的主动探索任务，几何一致的结构化空间记忆比单纯累积时序日志/观测帧的效率高至少一倍。
