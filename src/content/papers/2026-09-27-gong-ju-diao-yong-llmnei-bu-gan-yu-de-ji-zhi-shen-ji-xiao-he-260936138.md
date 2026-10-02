---
title: When Does Correction Become Repair? Mechanistic Auditing of Internal Interventions
  in Tool-Using LLMs
title_zh: 工具调用LLM内部干预的机制审计：校正何时成为真实修复
authors:
- Jiayi Li
- Ruizhe Li
affiliations:
- University of the Chinese Academy of Sciences
- School of Computer Science, University of Birmingham
arxiv_id: '2609.36138'
url: https://arxiv.org/abs/2609.36138
pdf_url: https://arxiv.org/pdf/2609.36138
published: '2026-09-27'
collected: '2026-10-02'
category: Agent
direction: Agent 工具调用决策内部干预审计
tags:
- LLM Agent
- Tool Calling
- Activation Steering
- Mechanistic Auditing
- Intervention Evaluation
one_liner: 提出SAKIKO审计框架，区分工具调用LLM决策的行为偏移与真实修复，严格验证内部干预效果
practical_value: '- 做Agent工具调用干预时，不能只看整体准确率提升，要同时审计三类效果：错误修正的目标到达率、原正确决策的误伤率、统计显著性，避免看似提升实则引入更多隐性错误

  - 多分类决策空间的内部Activation Steering，需要按定向错误通道（比如应该调工具却直接回答）分别训练转向向量和触发路由，不要用全局统一的干预向量，效果会更精准

  - 上线新的Agent干预策略前，可复用SAKIKO的统计许可流程，用预注册的置信区间阈值替代单点估计，避免小样本乐观估计导致的线上故障'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前工具调用LLM的预执行决策（直接回答/调工具/要信息/拒答）常出错，现有内部激活干预方法仅看整体准确率，无法区分是真的把错误修正为正确结果，还是仅转移到另一类错误，甚至误伤原本正确的决策，容易高估干预效果，引发线上风险。

### 方法关键点
- 定向错误通道建模：将错误按「正确行为→实际输出」的方向拆分独立通道，每个通道单独训练单位范数转向向量
- 路由触发机制：第一遍推理读取中间层隐藏状态，用线性路由判断是否触发对应通道的干预，仅匹配样本执行第二遍推理注入转向向量
- 目的地解析验证：跟踪干预后决策的完整流向，区分错误样本的「保留原错误/到正确目标/转到其他错误」，以及原正确样本的「保留正确/被误伤」
- 统计许可流程：预注册阈值，只有干预的目标到达率、误伤率、置信区间全部满足要求才认证为有效修复，否则拒绝。

### 关键结果
在When2Call、MetaTool基准上测试7个3.8B-9B LLM，对比随机向量、符号反转、层错配等baseline：
- 5个模型的定向干预实现正收益，Qwen2.5-7B锁死测试集净收益+79，Phi-3.5净收益+55；所有59个预算匹配的随机方向都达不到校准后的目标收益（p=0.017）
- 看似有效的干预可能存在严重问题：Phi-3.5的+55净收益干预，误伤了52/93个它触发的原正确决策；Qwen3-4B、Gemma-2-9B的正向点估计因置信区间不达标被拒绝认证。

### 核心结论
工具调用Agent的内部干预中，行为偏移不等于真实修复，整体准确率提升无法掩盖隐性的错误转移和正确决策误伤。
