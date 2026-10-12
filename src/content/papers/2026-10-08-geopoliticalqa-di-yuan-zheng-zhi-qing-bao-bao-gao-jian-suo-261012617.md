---
title: 'GeopoliticalQA: Benchmarking Retrieval and Generation over Intelligence Reports'
title_zh: GeopoliticalQA：地缘政治情报报告检索与生成基准测试集
authors:
- Veronika Solopova
- Ivan Havlytskyi
- Viktoria Skorik
- Ostap Vykhopen
affiliations:
- Mantis Analytics
- European Union Horizon Europe
arxiv_id: '2610.12617'
url: https://arxiv.org/abs/2610.12617
pdf_url: https://arxiv.org/pdf/2610.12617
published: '2026-10-08'
collected: '2026-10-12'
category: RAG
direction: 垂直领域RAG · 基准构建与性能评测
tags:
- RAG
- Benchmark
- Domain-specific QA
- Retrieval
- LLM-as-judge
one_liner: 开源地缘政治情报领域RAG基准，评测15款检索系统与6款开源大模型性能
practical_value: '- 垂直领域RAG数据集构建可复用「先文档画像限定问答范围，再生成匹配内容的问答对」的流程，避免生成不符合文档定位的无效问题，大幅降低标注成本，适合电商商品规则、商家资质、服务协议这类异构垂直文档的数据集搭建

  - 检索系统选型无需盲目追求大参数量embedding模型：中规模开源embedding（如bge-m3）性能可优于参数量大10倍的模型及商用API，BM25在实体密集的垂直领域表现极强，可作为基线优先验证，降低检索模块部署成本

  - 垂直领域RAG评测可采用LLM-as-judge方案，调优prompt后低推理成本的大模型评分可达到人类标注员的一致水平，适合电商大促、广告投放这类需要快速迭代评测的场景

  - 复杂推理类需求（如用户风险预判、多商品对比、优惠规则计算）的性能瓶颈不在检索而在生成侧，即使给gold context，小模型的不合理拒答、幻觉问题仍远高于中大型模型，可针对性做生成侧prompt优化或领域LoRA微调'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
地缘政治情报报告是高价值专业知识载体，涵盖冲突、制裁、供应链风险等多维度信息，但这类文档类型异构（包含政策简报、评估报告、数据手册等），大量内容涉及不确定性表述、推理判断与风险预测，现有通用RAG基准未覆盖该场景，无法验证系统在专业分析类文档上的检索与生成性能。
### 方法关键点
- 语料采集：通过多Agent浏览器自动化爬取415份2022年后发布的开源地缘政治报告，覆盖9类机构来源，最大化地域、立场、文档类型的多样性，无付费墙内容
- 问答对生成：先对每份文档做结构化画像，标注可回答/不可回答的问题范围，再匹配适配的分析师角色生成4类问答对（事实、推理、对比、风险导向），共生成5525个带证据引用的grounded问答对
- 质量校验：验证LLM-as-judge方案的有效性，GPT-5.4的评分与人类专家标注的一致性达到人类标注员之间的互信水平，可低成本完成全数据集质量校验
### 关键结果
- 检索侧：文档级召回所有模型R@10≥0.93，区分度极低；chunk级nDCG@10中，568M参的bge-m3达到0.785，与8B参的Qwen3-Embedding持平，显著优于OpenAI、Mistral等商用embedding API，BM25也达到0.787的同等性能
- 生成侧：给定gold context的条件下，24-70B中大型模型整体得分2.53/3，优于7-12B小模型的2.35/3；但风险导向类问题最优模型也有70%的回答存在瑕疵，推理类问题瑕疵率达47%
### 核心结论
垂直领域RAG的瓶颈已逐步从检索侧转向生成侧，即使检索到全部正确证据，大模型针对推理、对比、风险评估类复杂问题的忠实生成能力仍有较大缺口。
