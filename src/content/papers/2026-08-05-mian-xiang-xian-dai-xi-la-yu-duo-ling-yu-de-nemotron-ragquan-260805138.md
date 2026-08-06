---
title: 'Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding
  Generation for Modern Greek across Specialist Domains'
title_zh: 面向现代希腊语多领域的Nemotron RAG全栈适配方案
authors:
- Ayoub Kirouane
- Christos Petrocheilos
affiliations:
- Sophea AI
- KIEFER SA, Athens, Greece
arxiv_id: '2608.05138'
url: https://arxiv.org/abs/2608.05138
pdf_url: https://arxiv.org/pdf/2608.05138
published: '2026-08-05'
collected: '2026-08-06'
category: RAG
direction: RAG多语言适配 · 低资源语言优化
tags:
- RAG
- Low-resource Language
- Cross-encoder
- LoRA
- MoE
- Retrieval
one_liner: 从零构建希腊语RAG语料与基准，全链路适配Nemotron，大幅提升多领域检索与生成性能
practical_value: '- 低资源/垂直领域RAG落地优先测试BM25基线，不要盲目直接上线大参数多语种Embedder，该研究中8B现成多语种Embedder在希腊专业领域的表现显著差于无参数BM25

  - 构造检索模型训练用的合成query时，必须用真实用户query做few-shot风格对齐，该操作将nDCG@10相对BM25的提升翻倍，且需注意合成query的效果是生产环境的上限，避免对线上收益过度乐观

  - 检索系统不要只选用纯稠密或纯词法检索，用RRF融合BM25与适配后的稠密模型，无需复杂调参即可在域内、域外场景都拿到稳定增益

  - 评估重排等模块时必须加入无模块基线（如不做重排的一阶检索结果），避免引入负收益的模块，该研究中初期测试现成跨编码器的收益为0甚至为负'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现代希腊语未被Nemotron等主流检索模型、BEIR/MIRACL等通用多语种检索基准覆盖，而希腊法律、能源、金融、医疗等领域的长文本专业场景恰好是RAG的核心落地场景，且无原生可用的大规模训练语料与评测基准，现成多语种模型在该场景表现极差。

### 方法关键点
- 语料构建：清洗得到65773条跨5个领域的检索对，合成query时基于真实用户query做few-shot风格对齐，避免生成不符合用户习惯的短关键词query；每个query匹配约6个同领域hard negative，剔除标签冲突样本；将max_len设为4096适配希腊长文本（默认512会截断87%的训练对）
- 检索链路：全量微调1B Nemotron embedder，用RRF融合稠密检索结果与BM25结果；适配1B cross-encoder做重排，采用pointwise BCE loss训练
- 生成侧：LoRA微调30B-A3B MoE模型作为grounded reader，训练数据混合4万条带引用、拒答标注的监督样本与20万条希腊指令数据，缓解灾难性遗忘
- 基准发布：推出HERA希腊RAG评测基准，含4946条多上下文、带拒答标注、多难度的评测样本

### 关键结果
域内1B适配后embedder的nDCG@10从0.362提升至0.835，超BM25 0.08；通用域上适配后的模型语言能力迁移，比未适配base高0.399，但仍低于BM25，RRF融合后比纯BM25高0.027。适配后的cross-encoder比一阶检索提升nDCG@10 0.047，现成跨编码器初期测试无收益甚至负增益。LoRA微调后的MoE reader答案正确率从29.4%升至66.9%，忠实度从25.2%升至84.5%。

> 最值得记住的结论：上线更大参数模型前先测准基线，垂直/低资源场景下语言与领域适配的收益远高于参数规模的收益
