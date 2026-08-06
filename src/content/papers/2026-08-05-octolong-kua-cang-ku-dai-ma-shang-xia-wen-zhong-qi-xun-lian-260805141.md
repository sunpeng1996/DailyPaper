---
title: 'OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context
  Modeling'
title_zh: OctoLong：跨仓库代码上下文中期训练增强长上下文建模能力
authors:
- Indraneil Paul
- Falko Helm
- Goran Glavaš
- Iryna Gurevych
affiliations:
- TU Darmstadt
- University of Würzburg
- UKP Lab
- Center for Applied Cybersecurity ATHENE
- CAIDAS
arxiv_id: '2608.05141'
url: https://arxiv.org/abs/2608.05141
pdf_url: https://arxiv.org/pdf/2608.05141
published: '2026-08-05'
collected: '2026-08-06'
category: LLM
direction: 长上下文LLM · 训练数据工程
tags:
- Long-Context-LLM
- Data-Engineering
- LLM-Training
- Code-LLM
- Agent-Capability
one_liner: 提出跨仓库高依赖长代码数据构建流水线，训练多尺寸开源长上下文LLM，性能优于18个主流基线
practical_value: '- 训练长上下文Agent/LLM时可复用跨依赖数据构建思路：针对业务场景（如用户全链路行为、多轮对话历史）挖掘高依赖长序列，而非单纯拼接无关联长文本，可大幅提升长程记忆和推理能力

  - 长上下文微调后可采用预训练checkpoint与微调后checkpoint 1:9线性融合的trick，避免短上下文任务性能退化，适配推荐/广告场景同时需要短query理解和长用户行为建模的需求

  - 长上下文SFT时混合不同长度、不同领域的指令数据，无需分多阶段扩展上下文长度，单阶段即可获得稳定效果，降低训练成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长上下文训练数据多为书籍、论文、单仓库代码，普遍缺乏高密度长距离依赖，单纯拉长上下文长度会导致长程推理能力不足、"lost-middle"问题严重，无法满足Agent、RAG等场景对长上下文理解的需求。

### 方法关键点
- 提出OctoLong数据流水线：结合AST解析器、LSP语言服务、包管理器，在容器化环境中递归跨仓库检索代码依赖，BFS序列化生成最高达百万token的高依赖长代码上下文，共产出6.2B token高质量数据
- 训练流程：将占比12%的OctoLong数据混入总计50B token的长上下文微调（LCFT）语料，基于Qwen3基座单阶段扩展上下文到128K，再用10B token混合领域指令数据做SFT，训练前做1:9线性融合预训练和LCFT checkpoint避免短上下文退化
- 训练优化：采用ABF RoPE缩放（base频率提升到10M）、DeepSpeed-Ulysses序列并行、Liger kernel优化，128K上下文打包效率达99.87%

### 关键结果
对比18个开源长上下文LLM基线，OctoLong-Instruct全尺寸段均取得领先：14B版本长代码任务LooGLE得分39.88、通用长上下文LongBench得分41.36、Agent工具调用BFCL得分67.31，均优于同尺寸Qwen2.5-14B-Instruct-1M；仅替换12%的常规长语料为OctoLong数据，即可让8B模型长代码任务提升3.38分、Agent任务提升3.91分，无短上下文性能损失。

> 最值得记住的结论：长上下文能力的核心不是输入长度，而是训练数据的长距离依赖密度，高依赖长序列数据带来的收益远高于单纯拉长无关联文本长度。
