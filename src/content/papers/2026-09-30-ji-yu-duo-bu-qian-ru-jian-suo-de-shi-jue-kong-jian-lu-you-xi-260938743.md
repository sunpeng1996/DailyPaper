---
title: Learning to Route in Visual Space via Multi-Step Embedding Retrieval
title_zh: 基于多步嵌入检索的视觉空间路由学习
authors:
- Tianyu Chen
- Mingyuan Zhou
- Jiaxing Wu
affiliations:
- The University of Texas at Austin
- Google DeepMind
arxiv_id: '2609.38743'
url: https://arxiv.org/abs/2609.38743
pdf_url: https://arxiv.org/pdf/2609.38743
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent 多步视觉检索优化
tags:
- Multi-hop Retrieval
- Visual Agent
- Embedding Model
- Imitation Learning
- Reinforcement Learning
one_liner: 设计VHop基准与VHop-Router多步检索器，大幅提升视觉Agent搜索效率与成功率
practical_value: '- 多模态电商搜索（以图搜图、同款溯源、穿搭链路检索）可复用VHop-Router三段训练范式：SFT学正确链路→在线模仿学习学回退终止→RLVR优化最终成功率，相比直接升级LLM
  ROI高14倍

  - 落地LLM Agent时可复用「把多步导航逻辑下沉到检索工具而非让Agent处理」的架构思路，大幅减少LLM上下文Token消耗、降低API调用成本，适合成本敏感的ToC业务

  - 多步检索场景的训练评测数据可参考VHop的可控难度生成方法，低成本构造带干扰项、死路的标注数据，降低数据采集成本

  - 针对用户Query难描述的视觉搜索场景，可借鉴多步自回归检索设计，无需生成中间文本查询，降低文本描述偏差带来的性能损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前视觉Agent搜索依赖单步检索工具，遇到视觉线索难以用文本描述、中间证据不在Top-K召回结果的场景性能极差，且大量资源投入升级LLM的增益极低，核心瓶颈在于检索工具而非Agent本身。

### 方法关键点
- VHop是可控多步视觉检索基准，覆盖L1到L5共5级难度，支持精确/模糊两类Prompt，可自动生成带死路、干扰项的带验证标签的训练评测数据
- VHop-Router是端到端训练框架，基于Qwen3-VL-Embedding-2B用LoRA微调，分三阶段训练：SFT阶段用InfoNCE损失学习正确检索链路→在线模仿学习阶段学习回退、终止决策→RLVR阶段用可验证奖励强化最终答案成功率
- 推理时直接在视觉隐空间自回归检索，单次工具调用即可返回完整图像链路，无需Agent生成中间文本查询，兼容任意LLM Agent且不损失原生LLM能力

### 关键结果
在L4难度3-hop检索任务上，标准单步检索成功率仅3.7%，VHop-Router standalone可达76.3%；替换检索工具为VHop-Router后，Gemini 3.5 Flash Agent的成功率从32.7%提升至85.4%，增益达52.7pp，是升级到Gemini 3.1 Pro增益（3.7pp）的14倍；相比单步检索每步返回Top50的基线，VHop-Router上下文图像减少23×，API载荷降低35×，零样本泛化到真实场景测试集成功率比基线高10pp。

### 核心结论
视觉Agent搜索的核心瓶颈在检索工具而非LLM本身，把多步搜索逻辑下沉到检索层的ROI远高于升级LLM。
