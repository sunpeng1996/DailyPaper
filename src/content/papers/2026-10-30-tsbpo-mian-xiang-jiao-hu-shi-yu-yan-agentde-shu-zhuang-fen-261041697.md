---
title: 'TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language
  Agents'
title_zh: TSBPO：面向交互式语言Agent的树状分支策略优化方法
authors:
- Rui Yu
- Chong Mu
- Jinchuan Zhang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2610.41697'
url: https://arxiv.org/abs/2610.41697
pdf_url: https://arxiv.org/pdf/2610.41697
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 交互式Agent · 策略优化
tags:
- Interactive_Agent
- Policy_Optimization
- Credit_Assignment
- RL
- LLM_Agent
one_liner: 用树状采样-更新范式同时解决交互式Agent训练的采样、信用分配、多token损失聚合三个耦合问题
practical_value: '- 电商导购/智能客服类交互式Agent训练，可直接复用完整回合token损失聚合方案，取消单回复按长度归一化，实测可将指令有效性提升4个百分点、平均输出长度减少20token

  - 多轮交互场景RL训练可借鉴Root/Branch动态采样策略，在固定rollout预算下优先采样易产生正负结果对比的任务/状态，提升训练样本效率

  - 长Horizon交互任务的信用分配可复用「同前缀兄弟轨迹对比+同观测组步级优势」组合方案，不需要复杂回溯归因，WebShop场景实测可提升成功率5个百分点以上

  - 小参数LLM落地交互式Agent可先用大模型教师生成成功轨迹做SFT对齐再做RL，Qwen2.5-1.5B级别的模型即可达到SOTA水平，大幅降低部署成本'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
交互式语言Agent训练存在三个耦合痛点：固定rollout预算下无明确采样优先级、延迟反馈的信用分配无有效归因方案、多token动作的损失聚合易引入长度偏差，现有方法无法在一个训练loop内同时解决三类问题，导致长Horizon交互任务成功率低、输出有效性差。

### 方法关键点
- 两阶段初始化：先用大模型教师生成的成功交互轨迹做SFT，对齐交互协议，同时初始化可训练Actor和固定RL参考模型
- 似然拟合的Root/Branch分配器：融合历史成功/失败证据与语义相似样本证据，优先选择易产生正负结果对比的任务和状态做rollout，最大化固定预算下的训练信号密度
- 双维度信用分配：基于物理回放树的同前缀兄弟轨迹段对比得到轨迹优势，基于同任务/观测组的步级结果对比得到步级优势，两者相加作为总优势
- 完整回合损失聚合：每个完整回复内的token clipped surrogate直接求和，batch内按活跃回合数全局归一化，取消单回复内按token长度归一化，避免长度偏差

### 关键结果
基于Qwen2.5-1.5B backbone，在ALFWorld、WebShop两个标准交互式benchmark上测试：
- ALFWorld任务：seen任务成功率97.79%，unseen任务96.64%，领先同类SOTA方案
- WebShop电商交互任务：500个测试目标每轮6次随机采样，成功率81.07%，比去掉步级优势的消融版本高5.13个百分点
- 损失聚合消融：采用完整回合聚合比按token平均的方案，指令有效性从92.6%提升到96.59%，平均输出长度减少20个token

> 最值得记住的结论：交互式Agent RL训练中，优先采样易产生正负对比的样本、取消多token回复的长度归一化、结合兄弟轨迹与同观测组的局部信用分配，三者结合可大幅提升小模型交互性能，不需要复杂的算法设计。
