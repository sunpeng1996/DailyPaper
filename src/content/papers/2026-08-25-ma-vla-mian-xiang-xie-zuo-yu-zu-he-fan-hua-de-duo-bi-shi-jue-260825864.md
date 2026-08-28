---
title: 'MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional
  Generalization'
title_zh: MA-VLA：面向协作与组合泛化的多臂视觉语言动作模型
authors:
- Zaibin Zhang
- Junlan Xiao
- Zhongbo Zhang
- Yifan Wang
- Li Kang
- Yiran Qin
- Changxing Xia
- Heng Zhou
- Talas Fu
- Enshen Zhou
affiliations:
- Dalian University of Technology
- University of Oxford
- Sun Yat-sen University
- Shanghai Jiao Tong University
- University of Science and Technology of China
arxiv_id: '2608.25864'
url: https://arxiv.org/abs/2608.25864
pdf_url: https://arxiv.org/pdf/2608.25864
published: '2026-08-25'
collected: '2026-08-28'
category: MultiAgent
direction: 具身Agent 多臂协同泛化优化
tags:
- Embodied AI
- VLA
- Multi-Agent Collaboration
- Compositional Generalization
- Data Augmentation
one_liner: 提出支持角色无关的多臂协同VLA框架MA-VLA，可泛化到训练未见过的协作模式
practical_value: '- 任务拆解为原子子任务再分配的架构思路，可直接迁移至多Agent协同的推荐全链路场景，比如拆分召回、排序、素材生成为独立子任务分配给专属Agent执行

  - 训练阶段的角色shuffle数据增强策略，可用于优化推荐系统的跨场景泛化能力，消除对特定用户群、品类的固定角色依赖，提升OOD场景性能

  - 组合泛化的评测基准构建思路，可借鉴来构造推荐系统的域外测试集，验证模型在未见过的用户-商品交互组合下的鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型仅输入全局语言指令，无明确的单臂行为分配与组合机制，无法泛化到训练未观测过的协作模式，限制多臂具身系统的落地能力。
### 方法关键点
1. 提出MA-VLA统一框架，将协同任务拆解为中层原子prompt分配给各单臂，实现子目标显式定义与跨任务组合复用；
2. 引入Arm Shuffle训练策略，对单臂的观测、状态、分配的原子prompt做排列，强制角色无关的指令遵循，实现多臂组合泛化；
3. 构造训练集无对应协作模式的专属评测基准，专门验证未知协同场景下的模型性能。
### 关键结果
仿真与真实场景评测中，现有SOTA VLA在未见过的协作模式下基本失效，MA-VLA成功率显著领先，适配未知协同场景的能力大幅提升。
