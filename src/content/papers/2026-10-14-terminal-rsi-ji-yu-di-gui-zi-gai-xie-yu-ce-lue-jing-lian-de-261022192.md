---
title: 'Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite
  and Policy-Refine'
title_zh: Terminal-RSI：基于递归自改写与策略精炼的自改进终端Agent
authors:
- Junyao Yang
- Zongxia Li
- Yucheng Shi
- Zhongzhi Li
- Ruhan Wang
- Ruiwen Zhou
- Haitao Mi
- Shuicheng Yan
- Leowei Liang
affiliations:
- Tencent Hy Frontier
- National University of Singapore
- University of Maryland, College Park
- University of Georgia
- Indiana University
arxiv_id: '2610.22192'
url: https://arxiv.org/abs/2610.22192
pdf_url: https://arxiv.org/pdf/2610.22192
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 终端Agent 递归自优化
tags:
- Terminal Agent
- Recursive Self-Improvement
- Reward Shaping
- Credit Assignment
- PPO
one_liner: 交替执行递归自改写与带评论家继承的策略精炼，大幅提升终端Agent任务表现
practical_value: '- 奖励设计可复用FDR+SPR范式：电商/推荐多目标优化中，先按业务场景（如导购、下单、售后）归一化部分进度奖励，再给最终转化（如付款、好评）设置高优先级奖励，压制半完成行为的奖励占比，避免假阳性样本误导优化

  - 信用分配采用TB-GAE思路：多轮交互Agent（如智能导购、用户运营Agent）做PPO训练时，跳过无决策的观测token的衰减计算，仅在交互轮次边界应用衰减，消除冗长日志/回复长度对信用分配的偏差

  - 自迭代框架可复用RSR+RPR交替流程：先基于验证通过的高质量业务轨迹做SFT更新Actor，再继承上一轮的Critic网络做PPO微调，无需每次重置Critic，大幅降低持续迭代的训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
终端Agent的成功需通过可执行环境的严格验证，现有方案存在三大痛点：token生成与环境变化时钟不匹配，GAE按文本长度衰减导致信用分配偏差；递归自监督过程中Critic重置会丢失已学习的回报结构，直接继承又会出现预测误差漂移；单一全局奖励无法区分部分进度与严格成功，高得分失败样本会误导优化方向。
### 方法关键点
- 交替自改进框架：仅更新Actor的Recursive Self-Rewrite（RSR）阶段与联合优化Actor-Critic的Recursive Policy-Refine（RPR）阶段交替执行，Critic权重跨RSR阶段保留，每个RPR阶段先做4步Critic校准再联合训练
- 双层奖励设计：Family Dense Reward（FDR）按任务族历史分位归一化部分进度奖励；Success-Prioritized Reward（SPR）设置严格成功奖励高于所有失败样本的最大奖励，将失败样本的奖励占比从50.09%降至28.72%
- 轮次感知信用分配：Turn-Boundary Skip-Observation GAE（TB-GAE）跳过观测token的衰减计算，仅在交互轮次边界应用γ和λ衰减，消除文本长度对信用分配的干扰
- 分阶段训练策略：RPR-2阶段Actor学习率降为RPR-1的1/5，避免破坏继承的Critic结构
### 关键结果
基于Qwen3.8-27B基座训练，Terminal-RSI-27B在Terminal-Bench系列基准上四套件平均成功率达50.58%，较基座提升29.9个百分点；其中Terminal-Bench 4.0达19.84%、2.1达86.52%、Hard达79.00%；长horizon任务LHTB严格完成数从0/46提升至5/46，流程奖励从0.21升至0.37；训练集外SWR100任务成功率从3%翻倍至6%。

> 最值得记住：递归自改进的核心是交替完成高质量探索轨迹蒸馏与已学习价值结构的继承优化，无需每次迭代从零训练价值网络
