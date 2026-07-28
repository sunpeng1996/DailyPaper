---
title: 'From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent
  Protocol Distillation in Agentic Search'
title_zh: 智能搜索多智能体协议蒸馏：弥合专有与开源模型分布差异
authors:
- Junlin Liu
- Jiangwang Chen
- Zixin Song
- Shuaiyu Zhou
- Chunji Lv
- Hank Wu
- Kailin Jiang
- Jinyang Wu
- Bohan Yu
- Chenxi Zhou
affiliations:
- University of Chinese Academy of Sciences
- Tsinghua University
- Peking University
- Beijing Institute of Technology
- East China Normal University
arxiv_id: '2607.24280'
url: https://arxiv.org/abs/2607.24280
pdf_url: https://arxiv.org/pdf/2607.24280
published: '2026-07-26'
collected: '2026-07-28'
category: Agent
direction: 智能搜索Agent · 跨模型知识蒸馏
tags:
- Multi-Agent
- Knowledge Distillation
- Agentic Search
- Reinforcement Learning
- LLM Alignment
one_liner: 提出无需专有模型logits的多智能体协议蒸馏框架，将闭源智能搜索能力迁移到开源小模型
practical_value: '- 跨闭源-开源模型蒸馏时，可复用标准化JSON协议作为中间表示，避免模仿表层风格导致的性能下降，适合将GPT/Claude的搜索/推荐推理能力迁移到业务小模型

  - 离线多智能体生成训练数据的架构可直接复用：查询拆分子任务、并行检索、失败修复、结构化生成+质量校验的pipeline，可用来生成电商搜索/推荐的多轮推理训练样本

  - RL+蒸馏联合训练时，蒸馏损失权重建议取0.05，平衡蒸馏信号强度和模型原生推理能力，避免过度蒸馏导致的多步推理退化，可直接套用在Agent搜索推荐场景的对齐训练中

  - 专有模型仅用于离线生成结构化协议，不增加线上推理开销，适合业务侧低成本复用闭源大模型能力优化线上开源小模型的智能搜索/推荐Agent'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有智能搜索Agent依赖结果驱动的RL优化，监督信号极度稀疏；采用专有大模型作为教师做知识蒸馏时，受限于闭源模型无法输出logits、异构分词器不匹配，传统token级对齐方案不可行；直接模仿教师的自然语言推理轨迹会导致开源小模型出现严重风格漂移、幻觉，反而丢失原生推理能力，性能不升反降。
### 方法关键点
- 离线阶段基于专有大模型搭建多智能体流水线，完成查询分解、并行检索、失败搜索修复，将完整探索轨迹转换为标准化JSON协议，仅保留任务类型、推理计划、可溯源grounding事实等核心信息，完全剥离专有模型表层语言风格
- 训练阶段采用同模型双分支架构：特权分支额外输入结构化协议作为监督信号，普通分支仅输入原始查询，优化两分支token分布的KL散度作为蒸馏损失，联合GRPO的RL损失做端到端训练，梯度仅回传给普通分支
- 协议生成设置四层严格质量门：JSON schema校验、答案一致性校验、事实抽取溯源校验、信息泄露检测，过滤低质样本
### 关键结果
在7个单/多跳QA基准上测试，MAPD在Qwen3-1.7B上平均成功率达39.4%，比最优基线SDAR相对提升4.8%；在Qwen3-4B上平均成功率达44.4%，相对提升3.3%。该框架可无缝适配Claude、GPT、Gemini三类专有教师，无需调整流水线即可稳定获得收益。
### 核心结论
跨异构模型蒸馏的核心瓶颈是特权信息的质量而非训练机制，通过结构化表示剥离表层风格、保留核心推理逻辑，才能实现无负向迁移的能力迁移
