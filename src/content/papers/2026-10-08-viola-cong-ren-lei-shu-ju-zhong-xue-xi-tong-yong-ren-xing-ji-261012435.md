---
title: 'VioLA: Learning Generalist Humanoid Control Policies from Human Data'
title_zh: VioLA：从人类数据中学习通用人形机器人控制策略
authors:
- Mert Albaba
- Jens Beißwenger
- Anna Manasyan
- Daniel Marta
- Michael J. Black
- Wieland Brendel
- Andreas Krause
- Georg Martius
- Martin Riedmiller
affiliations:
- Vesoma
- ETH Zürich
- MPI-IS
- University of Tuebingen
- ELLIS Institute
arxiv_id: '2610.12435'
url: https://arxiv.org/abs/2610.12435
pdf_url: https://arxiv.org/pdf/2610.12435
published: '2026-10-08'
collected: '2026-10-11'
category: Other
direction: 人形机器人控制 · 跨域隐变量对齐
tags:
- Motion_Latent
- Zero_Shot
- Cross_Domain_Alignment
- Humanoid_Robot
- Policy_Learning
one_liner: 通过预测运动隐变量而非关节指令，用海量人类动作数据训练零样本泛用的人形机器人控制策略
practical_value: '- 跨域数据对齐思路可复用：当业务目标域标注数据稀缺时，可通过隐空间对齐将源域（如用户公开行为数据）与目标域（如业务私域行为）映射到同一空间，大幅扩充训练样本池

  - 解耦预测目标与底层执行的架构可参考：上层大模型仅输出高层语义隐变量，下游冻结轻量模型负责落地执行，既降低大模型学习难度，也可兼容不同执行端

  - 通用策略训练思路可迁移：避免针对每个细分任务单独微调，通过统一高层表示实现零样本任务泛化，可用于多场景通用推荐/广告排序模型训练'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
人形机器人控制存在两大痛点：一是动作空间大、关节耦合度高，直接学习关节指令难度大；二是机器人专属演示数据稀缺，现有策略需针对每个任务单独微调才能落地，无法零样本执行新指令，而海量人类动作数据无法直接作为训练标注。
### 方法关键点
1. 策略输出改为身体和手部运动隐变量而非底层关节指令，搭配预训练的冻结控制器将隐变量转成机器人可执行的关节动作
2. 训练人与机器人的运动编码器，将两者动作映射到同一隐空间，直接用人类动作数据作为策略训练标注，总训练数据达140.6M帧，其中93.2%来自人类
### 关键结果
真实机器人上零样本执行运动指令成功率100%，远超基线GR00T N1.7的16.7%和Ψ₀的0%；零样本操作任务成功率达88.6%，方法兼容2种VLA和1种世界动作模型backbone。
