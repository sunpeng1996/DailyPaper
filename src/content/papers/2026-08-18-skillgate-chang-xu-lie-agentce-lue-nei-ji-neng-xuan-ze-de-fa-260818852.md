---
title: 'SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents'
title_zh: SkillGate：长序列Agent策略内技能选择的训练方法
authors:
- Qingyao Li
- Wenxiang Jiao
- Shuai Shao
- Kangning Zhang
- Yuan Lu
- Yi Guo
- Weiwen Liu
- Weinan Zhang
- Yong Yu
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
arxiv_id: '2608.18852'
url: https://arxiv.org/abs/2608.18852
pdf_url: https://arxiv.org/pdf/2608.18852
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: Agent 策略内技能选择优化
tags:
- Skill Selection
- Credit Assignment
- GRPO
- Long-Horizon Agent
- RL for LLM
one_liner: 通过双独立信用通道解决长序列Agent技能选择的信用饥饿问题，大幅提升任务表现
practical_value: '- 电商导购/客服Agent等多技能场景可直接复用双信用通道设计，避免全局RL奖励稀释技能选择信号，无需额外训练独立路由模型，降低链路复杂度

  - 长序列多步推荐/导购Agent的RL训练中，对关键决策节点（如发券、跳转商品）可做token级信用隔离，仅给决策token分配局部奖励，避免后续执行误差惩罚正确前置决策

  - 技能/工具路由优化可复用「仅读取唯一正确技能才给正奖励」规则，避免Agent多读取技能浪费上下文窗口，同时降低误导性工具的误选率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长horizon Agent依赖大量外部技能库完成任务，现有基于全局任务结果的RL训练无法有效训练策略内的技能选择能力，核心障碍是「选择器信用饥饿」：技能选择仅占轨迹极少量token（中位数0.14%），全局奖励分配的信号被严重稀释，且后续执行失败会反向惩罚正确的技能选择，轨迹越长问题越严重，最长轨迹中正确选择的错误负向奖励占比超60%，但正确选技能本身可带来11.2pp的成功率提升。

### 方法关键点
- 轨迹token硬分割：仅技能名称对应token属于选择域，其余生成token属于执行域，两个域无重叠
- 双独立信用通道：执行域用常规GRPO全局任务奖励更新，完全屏蔽技能选择相关token；选择域用局部action级奖励，仅当轨迹仅读取唯一正确技能时给正奖励，按prompt组内动作归一化
- 权重归一化：两个通道的总损失权重保持相等，技能选择的权重与轨迹长度无关，彻底解决信号稀释问题

### 关键结果
在5个Agent基准、16候选技能slate下测试，9B参数模型：
- 对比仅用全局奖励的SkillRL基线，任务成功率从47.0%提升到53.2%，效果超过参数大40倍的参考模型
- 误导性技能的读取率降低2/3，单正确技能读取占比提升到75.4%，总技能读取次数降低41%
- 推理成本更低：技能读取次数、交互轮次、上下文token量均显著低于全局RL基线

**最值得记住的一句话**：当轨迹中混杂不同类型的决策时，对token支持做硬分割分配独立信用，比重新分配单一全局奖励的效率高得多
