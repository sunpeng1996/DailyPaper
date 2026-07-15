---
title: 'ABot-N1: Toward a General Visual Language Navigation Foundation Model'
title_zh: ABot-N1：面向通用视觉语言导航的基础模型
authors:
- Ruiyan Gong
- Yingnan Guo
- Junjun Hu
- Jintao Kong
- Xiaoxu Leng
- Tianlun Li
- Weize Li
- Fei Liu
- Zhicheng Liu
- Jia Lu
affiliations:
- AMAP CV Lab
- Alibaba Group
arxiv_id: '2607.10383'
url: https://arxiv.org/abs/2607.10383
pdf_url: https://arxiv.org/pdf/2607.10383
published: '2026-07-11'
collected: '2026-07-15'
category: Agent
direction: 具身Agent 视觉语言导航基础模型
tags:
- VLN
- Embodied Agent
- Chain-of-Thought
- Foundation Model
- Visual Reasoning
one_liner: 采用解耦认知与控制的快慢双架构，实现多场景可解释的SOTA视觉语言导航
practical_value: '- 快慢双架构解耦高层推理与底层执行的思路可复用在电商线下导购Agent、即时配送路径规划系统中，降低端到端决策的漂移风险

  - 像素级锚点作为多任务统一接口的设计，可迁移至多模态推荐系统的跨模态意图对齐环节，提升不同业务场景的泛化适配效率

  - 显式CoT推理+可追溯中间信号的设计，可用于优化Agent决策的可解释性，降低电商/本地生活场景下智能体错误决策的排查成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉语言导航（VLN）基础模型多采用端到端黑盒策略，存在坐标漂移、长尾语义处理差、可解释性弱的问题，难以同时兼顾通用性、鲁棒性与透明度。
### 方法关键点
采用快慢双架构解耦认知与控制，通过双模态信号引导决策：
1. 慢视觉语言推理模块执行显式Chain-of-Thought推理，输出像素级目标锚点作为多任务统一接口，适配点导航、POI导航、指令跟随、人员跟随等多类任务
2. 快动作专家模块结合文本提示与像素锚点，生成原生控制频率的连续航路点，通过像素锚点+语言推理轨迹打通高层意图与底层控制
### 关键结果
在城市级导航任务中POI到达率提升35.0%至77.3%，复杂室内/外场景成功率分别达95.4%/92.9%，在物体寻路、人员跟随、指令跟随任务上均保持SOTA鲁棒性，同步开源城市级点目标/POI导航基准。
