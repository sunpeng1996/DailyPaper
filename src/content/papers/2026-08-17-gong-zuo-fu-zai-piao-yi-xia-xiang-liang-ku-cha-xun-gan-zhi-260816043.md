---
title: 'Coverage Is Not Redundancy: Maintenance Cost and Exposure of Query-Aware Admission
  Indexes in Vector Databases Under Workload Drift'
title_zh: 工作负载漂移下向量库查询感知准入索引的维护成本与暴露边界
authors:
- Prashant Kumar Pathak
affiliations:
- Independent Researcher
arxiv_id: '2608.16043'
url: https://arxiv.org/abs/2608.16043
pdf_url: https://arxiv.org/pdf/2608.16043
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG 向量检索质量优化
tags:
- VectorDB
- Admission Control
- Workload Drift
- Retrieval Hub
- ANN Index
- RAG
one_liner: 揭示向量库准入索引覆盖≠冗余的结构性矛盾，推导观测受限的暴露下限并给出工程优化方案
practical_value: "- 搭建电商RAG客服/商品检索系统时，可复用sentinel query准入机制，入库阶段过滤通用FAQ、SEO作弊商品这类retrieval\
  \ hub，实测仅增加0.33%的pgvector入库开销，大语料库下几乎无感知\n- 生产环境用低召回ANN索引（如IVF-PQ）时，不要复用服务索引做准入校验，单独为sentinel\
  \ query开高召回探针，可避免索引召回低于0.5时的hub漏检问题，成本仅为固定大小sentinel集合的精确打分\n- 存在持续查询漂移的场景（如大促新热点、新品类上线），可复用论文预配置规则：按每个新兴查询区域的witness\
  \ deficit动态调整sentinel promotion速率，比固定速率降低24%的维护churn，同时满足暴露量约束\n- 检索端的score normalization（NNN、QB-Norm）对新兴区域的hub抑制效果远不如计数校验，可直接在检索层加$κ_S\
  \ ≥ \tau$的计数门控，和入库端校验达到相同抑制效果，无需修改入库链路"
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产级向量库支撑RAG系统时，常出现**retrieval hub**问题：单条向量（如通用FAQ、SEO作弊页面）被大量同主题查询召回，垄断结果严重影响体验。现有入库准入校验依赖sentinel query的reverse-kNN计数过滤hub，但工作负载漂移下sentinel集合需要在线维护，其维护成本与漏检风险的边界此前未被明确量化，甚至存在「覆盖一个区域就停止新增sentinel」的错误设计，导致hub漏检率极高。

### 方法关键点
- 提出**witness deficit（缺失覆盖质量）**核心指标：即过滤一个hub需要的sentinel数量减去现有sentinel数量的差值，推导得到观测受限的暴露下限$E ≥ m_{safe}+⌈(	au-c_0)^+/r⌉$，该下限与更新延迟无关，仅由区域检测阈值$m_{safe}$、准入阈值$	au$、初始sentinel数量$c_0$、单条sentinel贡献的计数$r$决定。
- 揭示结构性矛盾：监控策略只要覆盖区域（1条sentinel）就停止更新，但准入校验需要$	au$条sentinel的见证才会拒绝hub，两者的gap就是不可避免的暴露量。
- 提出召回感知修复方案：解耦服务索引与准入校验的召回配置，用高召回探针计算sentinel计数，避免低召回ANN索引导致的漏检。

### 关键结果
在8.8M向量的MS MARCO语料上测试HNSW、IVF-Flat、IVF-PQ三类索引：索引召回低于0.5时基线方案完全失去hub抑制能力，高召回探针方案可在所有召回点保持100%抑制率，暴露量稳定在精确检索的下限。在PostgreSQL/pgvector上实现原型，入库开销仅增加0.33%。COVID-19真实工作负载漂移测试中，暴露量完全符合推导的下限公式，$R^2=1.0$。对比检索端NNN、QB-Norm两类归一化方案，计数校验的暴露量仅为前者的40%，且是唯一能完全抑制hub的方案。

### 核心结论
向量库准入索引的覆盖不等于冗余，要过滤hub必须积累足够的sentinel见证，低召回索引下不能复用服务链路做准入校验。
