---
title: 'NEAR: Neighborhood-Aware Residuals for Memory Retrieval'
title_zh: 面向记忆检索的邻域感知残差框架NEAR
authors:
- Han Luo
- Zhan Zhuang
- Xu He
- Jujia Zhao
- Yu Li
- Suqin Yuan
- Dong Li
- Lei Feng
affiliations:
- Southeast University
- MemoraX AI
- Leiden University
- University of Sydney
arxiv_id: '2610.13314'
url: https://arxiv.org/abs/2610.13314
pdf_url: https://arxiv.org/pdf/2610.13314
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: RAG/Agent记忆检索 · 免训练嵌入优化
tags:
- Memory Retrieval
- Training-free
- Residual Embedding
- ANN Search
- RAG
- Agent Memory
one_liner: 免训练邻域感知残差检索框架，兼容任意冻结嵌入模型，大幅提升长上下文记忆检索效果
practical_value: '- 电商商品/内容向量召回、用户行为记忆检索场景可直接复用NEAR，无需微调现有嵌入模型，仅离线计算邻域残差+在线单ANN检索即可提升召回精度，完全兼容现有向量检索架构

  - Agent长时记忆模块可直接集成NEAR，实测对话记忆检索Recall@10最高提升14.76pp，下游QA准确率提升9.6pp，仅增加2.4倍以内检索延迟，多数业务可接受

  - 大规模向量库优化可参考NEAR的残差融合+4bit标量量化方案，量化后存储仅为FP32基线的36%，精度几乎无损失，适合降本增效的业务场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有嵌入检索仅依赖query与memory的向量相似度打分，当记忆库存在大量共享主题、实体的相似记录时，干扰项容易获得更高相似度分，挤掉正确证据样本，导致检索精度下降；现有优化方法要么需要微调嵌入模型，要么需要多轮检索，部署成本高，难以落地到存量业务。
### 方法关键点
- 免训练框架，兼容所有冻结嵌入模型，无需修改原编码器：离线为每个记忆向量计算其K近邻的平均方向作为局部参考，减去向量在该方向的投影得到残差表示
- 预构建球形K-means聚类的查询参考表，在线查询时无需先检索候选，直接查表组合得到查询侧的参考方向，计算查询残差
- 将原嵌入与多层残差表示加权拼接为统一的检索键，仅需一次ANN搜索即可完成融合打分，无需修改现有检索链路
### 关键结果
在8个长上下文检索基准（含对话记忆、金融/科学文档检索）上测试9款主流嵌入模型，所有模型均获得稳定提升：Qwen3-Embedding-4B的平均Recall@10从62.67提升至69.76，NDCG@10从47.88提升至55.33；下游LoCoMo对话QA任务准确率最高提升9.6pp；4bit量化下NEAR存储仅为FP32基线的36%，精度损失可忽略，检索延迟仅为基线的2.4倍以内。
> 最值得记住的一句话：记忆库中的相似干扰项不是检索的负担，反而是可用来构建局部参考、强化细粒度匹配信号的有效信息。
