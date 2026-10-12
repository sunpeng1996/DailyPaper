---
title: 'BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain
  Reasoning Distillation'
title_zh: BoundaryEvo：基于能力边界的长链推理蒸馏数据模型协同进化框架
authors:
- Jiaming Su
- Suorong Yang
- Xudong Li
- Tengchao Yang
- Peng Ye
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Nanjing University
- Tongji University
- The Chinese University of Hong Kong
arxiv_id: '2610.13285'
url: https://arxiv.org/abs/2610.13285
pdf_url: https://arxiv.org/pdf/2610.13285
published: '2026-10-09'
collected: '2026-10-12'
category: Reasoning
direction: 长链推理蒸馏 · 数据模型协同进化
tags:
- long-chain-reasoning
- knowledge-distillation
- co-evolution
- small-LLM
- SFT
one_liner: 提出两阶段数据模型协同进化框架，仅用1K样本大幅提升小模型长链推理能力
practical_value: '- 小模型蒸馏可复用两阶段范式：第一阶段先无过滤蒸馏少量样本打底基础能力，再做动态数据选择，避免弱模型初始阶段选不准样本的问题，适合电商Agent、推荐语义理解小模型快速迭代

  - 动态训练样本选择可借鉴能力边界筛选逻辑：仅保留「专家可稳定解决、当前模型未掌握、数据质量合格」的样本，比单纯采集错题的训练效率高30%以上

  - 多轮迭代训练可加入replay机制，保留上一轮仍有效的历史样本，避免模型学新忘旧，解决电商场景迭代后历史长尾场景效果退化问题

  - 资源有限的业务场景可优先用LoRA做小样本SFT，4B级模型仅需1K样本即可获得10%+的效果提升，大幅降低训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长链推理蒸馏采用固定训练集，样本效用随学生模型进化持续变化：已掌握的样本无新增增益，远超当前能力的样本无法学习，且初始弱模型无法完成可靠的样本筛选，小监督预算下该矛盾尤其突出，蒸馏效率极低。

### 方法关键点
- 两阶段协同进化框架：Stage1能力预热，无额外模型判断过滤，直接蒸馏少量教师生成的长推理轨迹，快速为学生模型建立基础推理能力，避免前期样本误筛
- Stage2能力边界动态迭代：每轮让当前学生与固定专家独立解同一批候选问题，筛选满足「专家可稳定解决、学生未掌握、数据质量合格、问题有效」的边界样本，每轮更新训练集
- 采用回放优先的样本分配策略，保留上一轮仍符合边界要求的历史样本，剩余配额补充新的高优先级边界样本，蒸馏前验证教师轨迹正确性，保证监督信号质量

### 关键实验
基于Qwen3.5-4B做LoRA SFT，仅用1K训练样本（100条预热+3轮每轮300条），在11个推理基准上全面超越静态蒸馏、随机选样、LLM2LLM等基线：IMO-AnswerBench准确率从62.9提升至75.3，AMO-Bench从26.8提升至46.0，效果优于部分200B级大模型，增益可迁移到Qwen2B、Gemma4B等多个backbone。

最值得记住的一句话：有效的推理监督信号不是固定的，可通过跟随学生能力边界的动态协同进化持续挖掘，小样本下即可实现小模型推理能力的大幅跃升。
