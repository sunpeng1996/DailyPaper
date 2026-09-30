---
title: Context Language Models
title_zh: 上下文语言模型：可原生自主管理上下文的大语言模型
authors:
- Rulin Shao
- Shannon Zejiang Shen
- Junjie Oscar Yin
- Yuetai Li
- Minheng Wang
- Hamish Ivison
- Radha Poovendran
- Nathan Lambert
- Teng Xiao
- Mike Lewis
affiliations:
- University of Washington
- Meta Superintelligence Labs
- MIT
- Trillium Labs
arxiv_id: '2609.37725'
url: https://arxiv.org/abs/2609.37725
pdf_url: https://arxiv.org/pdf/2609.37725
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 自主上下文管理优化
tags:
- Context Management
- LLM Agent
- KV Cache
- Reinforcement Learning
- Multi-Agent
one_liner: 提出将上下文视为可编辑文件的CLM架构，大幅提升长周期Agent任务性能并降低计算开销
practical_value: '- 长周期电商导购Agent可复用「上下文作为可编辑文件」的设计，允许Agent自主增删/压缩对话历史、用户偏好、商品浏览记录，避免长上下文溢出同时提升召回准确率，降低推理成本

  - 多Agent商品选品/营销策划场景可直接复用CLM的多上下文文件设计，每个Agent维护独立上下文，主Agent通过编辑上下文文件实现子Agent调度，相比传统消息队列通信开销可降低40%以上

  - LLM推理服务部署可直接落地Suffix Cache Reuse优化，对上下文编辑后的场景复用未修改后缀的KV cache，相比标准SGLang降低35%的服务端计算量，适合RAG/生成式推荐等频繁更新上下文的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型采用append-only的上下文更新逻辑，上下文管理依赖人工编写的外部调度器或固定功能工具，策略受限于人类先验，在长周期Agent任务、多Agent协同场景下易出现重要信息丢失、上下文溢出、推理计算开销过高等问题，现有方案的性能和效率均存在明显瓶颈。

### 方法关键点
- 架构设计：将上下文抽象为可编辑文件，大模型可通过通用Bash指令任意修改上下文内容，修改后自动同步到推理上下文，替代传统固定更新逻辑；天然支持多Agent部署，每个Agent对应独立上下文文件，支持动态创建、销毁和调度
- 策略优化：支持三层优化路径，零样本场景下可直接用现有LLM作为CLM；可通过自然语言指令或进化得到的技能文档引导CLM采用指定上下文管理策略；可通过带成功门控效率奖励的GRPO强化学习，同时优化任务准确率和推理开销
- 服务优化：提出Suffix Cache Reuse（SCR）机制，上下文编辑后复用未修改后缀的KV cache状态，仅重新预填充修改部分，大幅降低上下文修改后的重计算开销

### 关键结果
- 零样本CLM在BrowseComp-Plus深度研究基准上准确率超现有SOTA 11.4%，FLOPs降低21.5%；12小时EdgeBench长周期任务得分高5%，FLOPs降低59%；24小时多仓库Agent swarm任务相同计算下端到端速度提升65%
- 强化学习训练的Qwen3.5-9B CLM在BrowseComp-Plus上准确率较基线提升47.6%，FLOPs降低12%；搭配SCR优化的推理服务相比标准SGLang在相同性能下服务端计算量降低35%

### 核心洞察
上下文管理不需要依赖人工预设的策略或工具，让大模型自主探索上下文管理策略，效果和效率都能远超人类设计的方案，完全符合Sutton提出的「痛苦教训」规律
