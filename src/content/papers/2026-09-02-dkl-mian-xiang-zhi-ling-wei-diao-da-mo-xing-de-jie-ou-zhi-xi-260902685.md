---
title: 'DKL: Decoupled Knowledge Learning for Instruction-Tuned Language Models'
title_zh: DKL：面向指令微调大模型的解耦知识学习
authors:
- Kushagra Bhushan
- Meghanadh Pulivarthi
- Sai Krishna Reddy Sathi
- Gaurav Pandey
- Sonam Gupta
- Vineet Kumar
- Jaydeep Sen
- Yatin Nandwani
- Sachindra Joshi
- Dinesh Raghu
affiliations:
- IBM
- Indian Institute of Technology Madras
- Amazon
arxiv_id: '2609.02685'
url: https://arxiv.org/abs/2609.02685
pdf_url: https://arxiv.org/pdf/2609.02685
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: LLM知识注入 · 任务向量合并
tags:
- Knowledge Injection
- Task Vector
- LoRA
- Model Merging
- RAG
one_liner: 通过任务向量合并将Base LLM的扩展预训练知识注入Instruct LLM，无需重训指令微调能力
practical_value: '- 电商/客服Agent注入私域规则、商品知识库时，可复用DKL思路：先在同源Base LLM做领域语料的扩展预训练得到知识LoRA，再直接合并到现有Instruct
  LLM，避免重做IFT，大幅节省训练成本和数据依赖

  - 优化电商场景RAG系统时，可搭配DKL注入品类、活动、售后等领域知识，在检索失败场景下模型可 fallback 到参数知识，实测能提升近25个百分点的检索失败场景准确率，大幅减少问答幻觉

  - 训练领域知识LoRA时，可复用替换Base LLM的token embedding为目标Instruct LLM embedding的trick，解决两者特殊聊天token、系统指令token的分布不匹配问题，最高可提升6个百分点的检索失败场景准确率

  - 不需要生成覆盖全语料的海量合成QA，仅需50%语料量级的少量QA辅助，就能获得比RAFT/PA-RAG更好的效果，大幅降低合成数据生成的成本和时间'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG受限于检索质量，检索失败易出现幻觉；直接对Instruct LLM做扩展预训练（EPT）注入领域知识会导致指令跟随能力灾难性遗忘，重走指令微调（IFT）流程成本高且依赖私有IFT数据集；RAFT、PA-RAG等基于SFT的知识注入方案需要生成覆盖全语料的海量合成QA，成本高且易出现数据分布偏置，导致模型过拟合到高频概念。
### 方法关键点
- 基于任务向量思路，将Instruct LLM与同源Base LLM的权重差作为固定“指令跟随向量”，仅在Base LLM上做EPT训练得到“知识向量”，两者合并即可得到同时具备新知识和指令能力的模型，无需重训IFT
- 训练知识LoRA适配器时，替换Base LLM的token embedding及lm_head为对应Instruct LLM的权重，解决两者特殊指令token（如[INST]）的分布不匹配问题，提升适配器迁移效果
- 仅需添加少量（总字数为目标语料的50%）合成QA作为训练补充，无需覆盖全语料，QA直接拼接为普通文本参与预训练即可
- 最终部署时仅需将知识LoRA以超参数α缩放后合并到原Instruct LLM，α可在小验证集上快速搜索最优值
### 关键结果
在技术文档RedBook、开放域QuALITY数据集上测试，对比RAFT、PA-RAG、Chat-Vector基线：
- Mistral-7B-Instruct上，RAG检索失败场景准确率从基线的54.17%提升至79.26%，全测试集RAG准确率达86.58%，超出PA-RAG近2个百分点
- 训练耗时仅7分钟，远低于PA-RAG的43分钟，合成数据用量仅为RAFT的1/4、PA-RAG的1/20
- 适配0.6B到8B多种尺寸、不同架构的开源模型，效果均稳定优于基线
### 核心结论
给Instruct LLM注入领域知识无需在Instruct模型上做EPT或大量SFT，解耦知识训练与指令能力，通过任务向量合并即可低成本获得双能力在线的领域模型
