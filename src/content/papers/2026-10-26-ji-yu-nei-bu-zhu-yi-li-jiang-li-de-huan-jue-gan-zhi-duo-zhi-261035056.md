---
title: Hallucination-Aware Multi-Agent RAG via Internal Attention Rewards
title_zh: 基于内部注意力奖励的幻觉感知多智能体RAG框架
authors:
- Runsong Jia
- Qian Chang
- Mengjia Wu
- Ciprian Doru Giurcăneanu
- Jie Lu
- Yi Zhang
affiliations:
- University of Technology Sydney
- University of Auckland
arxiv_id: '2610.35056'
url: https://arxiv.org/abs/2610.35056
pdf_url: https://arxiv.org/pdf/2610.35056
published: '2026-10-26'
collected: '2026-10-27'
category: RAG
direction: 多智能体RAG · 幻觉抑制优化
tags:
- Multi-Agent RAG
- Hallucination Mitigation
- LoRA
- PPO
- Attention Head
- Reward Shaping
one_liner: 利用LLM内部注意力特征做幻觉奖励，训练多智能体RAG的角色LoRA，同步提升效果与降低幻觉
practical_value: '- 业务RAG场景（电商客服、商品问答、推荐理由生成）可复用「任务奖励+内部幻觉风险信号」的PPO训练范式，无需额外调用大模型做judge即可降低幻觉，节省推理成本

  - 多智能体RAG的角色拆分无需部署多套独立LLM，采用共享冻结主干+角色专属LoRA的实现方式，参数效率高、上线成本低

  - 幻觉检测无需依赖业务场景标注，可基于TruthfulQA预训练轻量化注意力头norm特征判别器，跨任务可迁移，无需每个场景重新训练

  - 电商生成式推荐、商品属性问答等高保真要求场景，可直接复用该奖励设计，在不损失回答准确率的前提下降低10%左右的幻觉率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多智能体RAG仅用EM、F1这类答案匹配度作为共享奖励，不会惩罚回答中超出检索证据的幻觉内容，最终生成的答案可能命中正确片段但掺杂大量无依据信息；而现有幻觉监督信号要么依赖外部大模型judge（调用成本高，不适合做RL稠密奖励），要么仅作用于生成阶段，无法回溯优化上游的查询规划、证据选择环节，幻觉根因无法彻底解决。

### 方法关键点
- 多智能体拆分：将RAG流程拆分为查询规划、证据选择、答案生成3个角色，每个角色用共享冻结主干+专属LoRA实现，无需独立部署多模型
- 幻觉风险critic设计：基于TruthfulQA的真假答案对，筛选出与真实性强相关的注意力头，用这些头的输出norm均值作为特征，训练轻量化MLP判别器，训练完成后永久冻结，RL阶段输出0-1的幻觉风险分
- 训练范式：先SFT暖启动3个LoRA，再用PPO做协同训练，共享奖励为「α*任务F1分 - λ*幻觉风险分」，所有角色同步更新各自LoRA参数，主干和critic全程冻结

### 关键实验
在3个基准（RAGTruth、HotpotQA、2WikiMultiHopQA）、3个主干（Qwen3-8B、Llama3-8B、Llama2-13B）上测试，对比MMOA-RAG等最强多智能体RAG基线：Qwen3-8B上平均R/A提升2.35个点，EM提升0.95个点，F1提升1.29个点；RAGTruth上的回答幻觉率（AHR）相对基线最高降低10.74个百分点，Llama3-8B和Llama2-13B上也分别降低5.62、3.34个百分点。

### 核心结论
大模型内部注意力头本身携带丰富的真实性信号，将其转化为奖励信号优化整个RAG链路，能在不增加推理成本的前提下同时提升任务效果和生成忠实度。
