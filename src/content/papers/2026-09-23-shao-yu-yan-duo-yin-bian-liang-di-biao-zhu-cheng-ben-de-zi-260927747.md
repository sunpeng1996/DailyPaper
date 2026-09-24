---
title: 'Less Language, More Latents: Annotation-Efficient VLAs for Driving'
title_zh: 少语言多隐变量：低标注成本的自动驾驶VLA模型
authors:
- Alexey Zakharov
- Kemal Oksuz
- Puneet K. Dokania
affiliations:
- Robert Bosch GmbH, Germany
- Five AI Ltd., United Kingdom
arxiv_id: '2609.27747'
url: https://arxiv.org/abs/2609.27747
pdf_url: https://arxiv.org/pdf/2609.27747
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: 自动驾驶VLA · 低标注训练优化
tags:
- VLA
- Low-resource Training
- Vector Quantization
- Latent Action
- Autonomous Driving
one_liner: 仅用5%语言标注，通过三阶段隐变量映射pipeline训练自动驾驶VLA，性能持平全监督基线
practical_value: '- 低资源任务可复用「无标注数据预训练生成隐变量码本+小标注子集模态对齐」的范式，大幅降低标注成本

  - 多模态指令调优场景可引入vector-quantised瓶颈压缩高层意图空间，提升跨模态映射稳定性

  - 落地大模型驱动的决策类Agent时，可优先将输出映射到预定义隐变量码本，降低端到端输出的不稳定风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLA是实现可解释、支持自然语言控制的自动驾驶核心方案，但训练依赖大量高成本的语言-轨迹配对标注，规模化落地难度极高。
### 方法关键点
提出LADA三阶段训练pipeline：
1. 用全量无标注观测-轨迹对训练带vector-quantised瓶颈的隐动作模型，生成高层车辆意图的紧凑码本；
2. 仅用<5%的有语言标注子集训练跨模态翻译器，将观测、语言指令映射到上述隐变量码本空间；
3. 用全量观测-隐动作对训练最终VLA，无需CoT、VQA等额外辅助监督信号。
### 关键结果
在Bench2Drive闭环基准上取得87.98的驾驶得分、70.46%的成功率，性能持平甚至超过全监督基线。
