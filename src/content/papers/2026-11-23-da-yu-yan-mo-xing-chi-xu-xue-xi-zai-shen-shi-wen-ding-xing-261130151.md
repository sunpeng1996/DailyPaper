---
title: 'Revisiting Continual Learning in Language Models: A Three-Interface Diagnosis
  of Stability and Plasticity'
title_zh: 大语言模型持续学习再审视：稳定性与可塑性的三接口诊断框架
authors:
- Keuntae Kim
- Beomseok Lee
- Hyunwoo Kim
- Yong Suk Choi
affiliations:
- Hanyang University
- LG Electronics
- KT Corporation
arxiv_id: '2611.30151'
url: https://arxiv.org/abs/2611.30151
pdf_url: https://arxiv.org/pdf/2611.30151
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM持续学习 · 遗忘诊断与性能恢复
tags:
- Continual Learning
- Catastrophic Forgetting
- Stability-Plasticity Dilemma
- LLM Fine-tuning
- Evaluation Framework
one_liner: 提出三接口诊断框架拆分LLM持续学习遗忘来源，证实多数遗忘为头- backbone不匹配导致
practical_value: '- 电商/Agent场景做LLM增量微调（新类目识别、新意图适配）时，旧任务性能下降优先做LM头重对齐，无需立刻调整backbone，replay/distillation类增量方法96~99%的性能损失可恢复，纯顺序微调也能恢复74%，大幅节省调优成本

  - 持续学习效果评估不要仅依赖最终训练头的准确率，可补充探针和表征分离度诊断，精准定位是表征漂移还是头不匹配问题，避免误判backbone的知识保留能力

  - 多场景增量适配选型时需注意：LoRA等参数高效微调虽然旧任务稳定性更高，但表征层面的新任务可塑性比全量微调下降50%以上，需根据业务对新旧任务的性能要求权衡方案'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM持续学习评估仅通过最终训练头的性能判断遗忘程度，无法区分性能下降是来自backbone表征退化还是头的读出不匹配，导致对模型稳定性（抗遗忘能力）和可塑性（新任务学习能力）的评估存在严重偏差，也无法定位遗忘根因。
### 方法关键点
- 设计三类评估接口拆分遗忘来源：①训练头：随backbone顺序更新的原生预测头，测量实际部署性能；②探针：冻结backbone后新训练的线性分类头，测量backbone保留知识的可恢复性；③backbone诊断：基于聚类/NCM/kNN的无分类器表征可分性指标，直接测量表征层面的漂移程度。
- 提出JLT（Just LM-Head Tuning）诊断方法：固定增量训练后的backbone，仅重优化LM头，量化可通过头对齐恢复的遗忘比例，将总遗忘拆分为头- backbone不匹配损失和表征漂移残差两类。
### 关键结果
覆盖7个文本分类/意图识别/关系抽取数据集，测试10种编码器/解码器backbone，对比12种主流持续学习方法：①训练头评估平均遗忘率达87.8%，探针评估遗忘率仅~2%；②replay/distillation类增量方法96~99%的性能损失可通过JLT恢复，纯顺序微调恢复率也达74%；③backbone层面稳定性与可塑性始终呈负相关（皮尔逊系数均值-0.74），现有方法未从表征层面解决稳定性-可塑性困境。

**最值得记住的结论**：LLM持续学习中的“灾难性遗忘”大部分是头与backbone的读出不匹配，而非backbone真的丢失了旧知识，遗忘不是单一的模型级指标，而是依赖评估接口的测量值。
