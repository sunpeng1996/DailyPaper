---
title: 'NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving
  MLLMs'
title_zh: NeuPAT：神经元感知可塑性分配调优 保留MLLM原生语言能力
authors:
- Jiayue Jin
- Jingwei Zhang
- Chen Wang
- Jing Liu
- Longteng Guo
affiliations:
- 复旦大学
- 中关村实验室
- 中国科学院自动化研究所
- 中国科学院大学
- 天津大学
arxiv_id: '2608.08107'
url: https://arxiv.org/abs/2608.08107
pdf_url: https://arxiv.org/pdf/2608.08107
published: '2026-08-07'
collected: '2026-08-13'
category: LLM
direction: 大模型多模态微调 · 灾难性遗忘缓解
tags:
- MLLM
- Catastrophic Forgetting
- Neuron-level Tuning
- Multimodal Adaptation
- Fine-tuning
one_liner: 通过神经元级差异化更新约束，MLLM多模态微调时保留原生语言能力且不降低多模态性能
practical_value: '- 开发电商多模态Agent（图文理解、直播解析、智能导购）时，可复用NeuPAT的差异化微调思路，避免多模态训练破坏LLM原生的语义理解、文案生成、逻辑推理能力

  - 做生成式推荐、多模态搜推的MLLM微调时，可直接引入轻量神经元探测流程，无需额外文本重训数据、无需修改模型架构，即可缓解语言能力退化问题

  - 大模型领域微调遇到旧能力遗忘问题时，可借鉴神经元重要性分群+差异化约束的思路，替代通用LoRA、数据重放等方案，平衡新旧能力保留'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM扩展为多模态大模型（MLLM）时，常规多模态指令微调会导致原生语言能力严重退化，平均降幅达39.8%；现有解决方案要么需要额外文本重训数据增加训练成本，要么需定制化修改模型架构提升复杂度，要么后处理模型合并会带来多模态/语言能力的强tradeoff，缺乏高效、架构无关的通用方案。
### 方法关键点
- 轻量探测阶段：用各2048条的文本、视觉小样本计算每个神经元的模态关联重要性得分，按得分将神经元分为语言关联、多模态关联、双模态共享、储备四类
- 差异化更新约束：微调时语言关联神经元完全冻结，多模态关联和储备神经元全量更新，双模态共享神经元通过参数范数、余弦相似度约束做限制更新，无需额外数据或架构修改
- 训练损失为原自回归损失加共享神经元约束项，适配任意Transformer结构的LLM
### 关键结果
在6个不同规模、不同系列的LLM上验证，对比Vanilla微调、LoRA、EWC、WINGS、模型合并等7种baseline：在11个语言基准上恢复94.5%的语言能力损失（Vanilla微调平均降5.07分，NeuPAT得分49.06分几乎追平原生LLM的48.99分），同时5个多模态基准平均得分仅比Vanilla微调高0.07分，无多模态性能损失。
### 核心结论
LLM神经元存在天然的模态功能异质性，差异化控制不同神经元的更新幅度，是比全局微调、LoRA、数据重放更高效的能力保留方案。
