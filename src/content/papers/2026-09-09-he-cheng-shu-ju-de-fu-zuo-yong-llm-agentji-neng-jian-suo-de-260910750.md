---
title: 'When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for
  LLM Agents'
title_zh: 合成数据的副作用：LLM Agent技能检索中的灾难性遗忘研究
authors:
- Syed Shariyar Murtaza
- Yifan Nie
- Utkarsh Soni
- Eugene Wen
- Arvid Frydenlund
affiliations:
- Manulife, Canada
arxiv_id: '2609.10750'
url: https://arxiv.org/abs/2609.10750
pdf_url: https://arxiv.org/pdf/2609.10750
published: '2026-09-09'
collected: '2026-09-11'
category: Agent
direction: Agent 技能检索 灾难性遗忘缓解
tags:
- LLM Agent
- Catastrophic Forgetting
- Skill Retrieval
- LoRA
- Synthetic Data
one_liner: 验证合成数据微调导致LLM Agent技能检索灾难性遗忘，提出带正则的LoRA方案兼顾分布内增益与OOD性能
practical_value: '- 做Agent工具/技能检索微调时，禁止直接用合成数据暴力LoRA微调，会导致真实/OOD场景Recall@10最高暴跌20%

  - 可直接复用4种遗忘缓解正则方案：embedding anchor、LwF、EWC、L2-init，效果接近，都能在不损失OOD性能的前提下，提升分布内召回13.98%

  - LoRA rank是控制性能-稳定性trade-off的核心参数，优先用低rank（如r=8）、仅微调attention层的保守配置，训练稳定性更高，种子敏感度极低

  - 重排器微调可加listwise LwF正则，能在不损失真实场景效果的前提下，提升分布内MRR最多16.2%'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM Agent依赖运行时检索外部技能库完成复杂任务，真实技能标注数据稀缺，业界普遍用合成数据微调检索模型，但此前未大规模验证合成数据是否会导致OOD场景的灾难性遗忘，直接影响线上部署的稳定性。

### 方法关键点
- 数据：基于34396个公开技能构建数据集，生成两类合成训练集：Track A（1.5万单正例对）、Track B（1.4万多正例对，含少量真实标注、paraphrase、多技能合成任务）
- 遗忘缓解策略：对比4种正则方案：① embedding anchor正则，惩罚微调后技能embedding与冻结预训练模型的偏差；② L2-init，约束LoRA参数接近初始化值；③ EWC，按参数重要性加权约束参数偏移；④ LwF，用KL散度约束微调前后的排序分布一致
- 模型架构：采用Qwen3-Embedding-0.6B做bi-encoder召回，Qwen3-Reranker-0.6B做cross-encoder重排，均基于LoRA微调

### 关键结果
- 暴力LoRA微调（r=16/32，全投影层微调）会让OOD场景Recall@10从0.85暴跌至0.65，分布内仅提升7.4%，得不偿失
- 4种正则方案效果接近，可完全保留OOD场景Recall@10（0.85不变），同时分布内Recall@10提升13.98%，超过暴力微调的增益
- 重排器加listwise LwF正则后，分布内MRR从0.582提升到0.744，真实OOD场景MRR稳定在0.78左右无损失

**最值得记住的结论**：用合成数据微调检索/重排模型时，优先采用低秩LoRA+遗忘缓解正则的保守配置，才能兼顾分布内增益和线上OOD场景的稳定性。
