---
title: Query Generation with Direct Preference Optimization for Document Expansion
  in E-commerce Search
title_zh: 基于直接偏好优化的电商搜索文档扩展查询生成方法
authors:
- Kaihao Li
- Feng Liu
- Juexin Lin
- Xunfan Cai
- Zhen Yang
- Tony Lee
- Ciya Liao
affiliations:
- Walmart Global Technology
arxiv_id: '2610.04352'
url: https://arxiv.org/abs/2610.04352
pdf_url: https://arxiv.org/pdf/2610.04352
published: '2026-10-03'
collected: '2026-10-06'
category: QueryRec
direction: 电商搜索查询生成 · DPO偏好优化
tags:
- Doc2Query
- DPO
- Document Expansion
- E-commerce Search
- Query Generation
one_liner: 将DPO应用于Doc2Query优化电商文档扩展查询生成，结合相关性过滤上线后获显著效果
practical_value: '- 做电商Doc2Query类任务时，可在SFT后加DPO微调，用已有相关性模型自动构造胜负query对，无需额外人工标注，能降低50%左右无关生成结果，且不损失新token数量

  - 生成后加相关性过滤层，选择95%召回阈值的精确匹配概率截断，能额外过滤14%+无关query，平衡精度和新token覆盖率，适合生产落地

  - 解码策略优先选beam search（beam size=10，禁止2元ngram重复），比top-k/top-p采样的精确匹配率高4%+，无关query少近2%，检索结果更稳定

  - 算力充足的场景可替换T5为Mistral-7B做LoRA微调，精确匹配率升2%，无关query降22%+，尤其适合泛品类、需世界知识的商品查询生成'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索普遍存在词汇不匹配问题，用户搜索词与商品描述语言体系差异大，传统Doc2Query生成的查询易出现幻觉、重复已有内容，仅靠后处理过滤无法解决生成器本身的质量缺陷，RL类优化方法又会损失查询多样性，亟需兼顾相关性和多样性的查询生成方案。
### 方法关键点
- 两步训练：先SFT微调T5-base/Mistral-7B等基础序列到序列模型生成商品对应查询；再用内部相关性模型对生成结果打分，构造「商品-胜查询（精确匹配）-负查询（无关）」三元组，用DPO做偏好微调，β取0.1效果最优
- 后处理过滤：生成结果保留相关性模型输出精确匹配概率≥95%召回阈值的查询，仅将原商品没有的新token加入索引
- 解码选择beam search（beam size=10，禁用2元重复ngram），平衡相关性和生成稳定性
### 关键实验
基于Walmart 2年用户行为数据构造6400万商品-查询对训练集，离线对比基线Doc2Query：单DPO微调即可提升精确匹配率8.07%，无关生成减少49.87%；叠加相关性过滤后精确匹配共提升9.63%，无关生成减少64.48%，新token数量仅减少0.1个，几乎不损失多样性。线上A/B测试NDCG@5提升0.93%，搜索会话加购率提升0.36%，已全量上线Walmart全站；算力充足场景下用Mistral-7B做SFT，比T5-base精确匹配率提升2%，无关生成减少22.84%。
### 核心结论
DPO微调+后处理过滤的组合方案，在不损失生成多样性的前提下可大幅提升Doc2Query的生成质量，生产落地成本低、收益明确
