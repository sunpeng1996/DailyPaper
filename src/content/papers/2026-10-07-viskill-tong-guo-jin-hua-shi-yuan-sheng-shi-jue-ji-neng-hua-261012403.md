---
title: 'ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills'
title_zh: ViSkill：通过进化式原生视觉技能强化VLM智能体
authors:
- Hongxing Li
- Dingming Li
- Yixin Li
- Yong Du
- Wenqi Zhang
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
arxiv_id: '2610.12403'
url: https://arxiv.org/abs/2610.12403
pdf_url: https://arxiv.org/pdf/2610.12403
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: VLM Agent · 视觉技能闭环优化
tags:
- VLM-Agent
- Skill-Library
- Reinforcement-Learning
- Visual-Native-Skill
- PPO
one_liner: 提出视觉原生技能卡片与闭环优化框架，大幅提升VLM Agent空间任务成功率与收敛速度
practical_value: '- 电商视觉交互类Agent（如虚拟试穿引导、直播间智能助手）可复用视觉原生技能卡设计，替代文本技能，保留空间布局/操作路径信息，避免文本抽象的信息损失

  - Agent技能库的质量+novelty双门控、冷启动初始化策略可直接复用，平衡技能库的多样性和有效性，解决冷启动阶段无有效经验引导的问题

  - 技能引导的奖励设计可迁移到RL优化的搜索推荐场景（如多步转化路径优化），给部分符合高价值路径的中间行为发放辅助奖励，缓解稀疏奖励问题

  - 技能库和策略协同进化的闭环设计可复用，技能库提供上下文引导和奖励信号，优化后的策略反过来产出更高质量技能，形成正向循环'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有技能增强Agent大多为文本中心化，将空间布局、动作-状态对应关系线性化为文本，丢失关键几何结构信息；且技能构建与策略优化解耦，未利用二者双向增益，导致VLM Agent在空间视觉交互任务上样本效率低、性能差。

### 方法关键点
- 设计原生视觉技能卡片：将成功轨迹的标注帧+策略蒸馏的策略描述渲染为统一图像，保留空间和过程上下文，同时存储几何描述符、效用、使用计数元数据
- 几何感知技能检索：基于当前任务的几何特征和技能的历史效用加权计算匹配分，高于阈值的技能作为视觉上下文输入VLM
- 闭环优化：成功轨迹经过质量（长度不超过最优解）、新颖性（和现有技能匹配度低于阈值）双门控后蒸馏为新技能入库，容量满时按效用-频率得分淘汰低价值技能
- 技能引导奖励：对失败轨迹中与检索技能对齐的部分发放辅助奖励，和PPO联合优化策略；可选冷启动机制预填充少量种子技能加速早期学习

### 关键实验
在Sokoban、FrozenLake、PrimitiveSkill三类2D/3D空间交互任务上测试，对比GPT-5、o3、Gemini 2.5 Pro等闭源模型，以及Qwen2.5-VL、VAGEN、AtlasVA等开源基线。ViSkill整体成功率0.89，加冷启动后达0.91，优于所有基线，收敛速度比标准PPO快30%以上；视觉技能卡比文本技能方案成功率高20%以上。

### 核心结论
对于空间视觉交互类Agent，原生视觉技能的信息密度和泛用性远高于文本抽象的技能，技能库与策略的协同进化是提升性能和样本效率的核心路径
