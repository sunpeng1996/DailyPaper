---
title: 'LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent'
title_zh: LuthorSQL：作为慢LLM Agent快思考模块的单轮Text-to-SQL模型
authors:
- Ibrahim Memon
- Armin Karamzade
- M. Hanif Jhaveri
- Roy Fox
affiliations:
- UC Irvine
- Independent Researcher
arxiv_id: '2611.17780'
url: https://arxiv.org/abs/2611.17780
pdf_url: https://arxiv.org/pdf/2611.17780
published: '2026-11-12'
collected: '2026-11-17'
category: Agent
direction: Agent快慢系统级联优化
tags:
- Text-to-SQL
- System 1
- Model Cascade
- LoRA
- Cost Optimization
- Edge Inference
one_liner: 单轮非自回归7B Text-to-SQL模型作为System1前置LLM Agent，降本33%不损精度
practical_value: '- 可直接复用快慢系统级联架构：电商/互联网企业的运营数据查询、推荐特征查询等高频常规请求，用本地小模型承接，复杂长尾请求才调用大模型API，可降本30%以上，同时避免内部敏感数据泄露

  - 结构化槽位填充+执行验证的设计可迁移到规则明确的生成场景：比如搜索query改写、商品属性生成等，约束输出到固定槽位+后置验证，能大幅降低小模型的幻觉率，工程实现简单

  - 置信度路由Trick可直接复用：用小模型输出的top2结果分差作为路由阈值，不需要额外训练路由模型，可快速复用到搜索query分类、推荐粗排结果过滤等场景

  - 跨数据源零样本迁移思路可复用：先生成语义无关的中间表示再转译不同数据源格式，适合电商多数据源查询、多平台内容生成等场景，无需为每个数据源单独训练模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型Agent做Text-to-SQL精度高但成本高昂，Claude Opus 5.5处理1万次/天的查询年成本超7万美元，且企业内部查询发送到外部API存在数据泄露风险；而80%以上的企业内部数据查询都是高频常规请求，可通过本地模型承接。
### 方法关键点
- 基于冻结的OmniSQL-7B主干训练两个LoRA适配器：生成器单轮前向并行预测结构化查询计划的所有槽位，无需自回归逐token生成；验证器对最多32个候选SQL的执行结果打分，选最优输出
- 结构化查询计划覆盖84.6%的BIRD基准查询，自动基于外键图生成JOIN逻辑，避免小模型生成语法错误或幻觉字段
- 级联路由无需额外训练模型，直接用验证器输出的top2结果组分差作为置信度阈值，低于阈值才路由到LLM Agent（System2）处理
### 关键结果
- 单模型在BIRD隐藏测试集执行精度达68.03%，单GPU单query耗时0.84s，8-bit量化后仅需9GB显存；零样本迁移到Snowflake、BigQuery等5种SQL方言，精度最多下降3.1个点
- 与Claude Opus级联后，在227个大模型训练截断后发布的新数据库查询上，本地承接近50%查询，API成本降低33.3%，精度与纯调用大模型无统计差异
- 污染探测显示Claude Opus可原样复现48%-92%的公开基准Gold SQL，但工具调用能力在重命名schema和新数据集上保持稳定
### 核心结论
企业级AI应用无需全量请求调用大模型，用本地小模型承接大部分常规请求、复杂请求路由到大模型的级联架构，可在不损失精度的前提下大幅降本、保护数据隐私
