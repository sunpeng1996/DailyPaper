---
title: 'RAGAL: A Frugal, Fully Local Retrieval-Augmented Assistant for Technical Support
  at a Government Agency'
title_zh: RAGAL：面向政府机构技术支持的低成本全本地检索增强助手
authors:
- Dan Musetoiu
affiliations:
- Agency for Financing Rural Investments (AFIR), Romania
arxiv_id: '2607.18756'
url: https://arxiv.org/abs/2607.18756
pdf_url: https://arxiv.org/pdf/2607.18756
published: '2026-07-21'
collected: '2026-07-22'
category: RAG
direction: 本地化RAG · 低资源部署
tags:
- RAG
- Local-LLM
- Embedder-Finetuning
- Low-Resource
- On-Premise
- Zero-Egress
one_liner: 零数据流出、单8GB消费级显卡约束下落地全本地RAG政务技术支持助手
practical_value: '- 多域语料微调Embedder时必须做分域评测：单域微调会静默降低其他未训练域的检索效果，这类劣化无法通过全局评测发现，电商/推荐场景下商品、用户评论、平台规则等多域语料微调时可直接复用该经验

  - 8GB消费级显卡微调Embedder的可复用方案：8-bit优化器+梯度检查点可解决Windows平台显存静默溢出问题，72分钟即可完成568M参数bge-m3全量微调，适合小成本团队落地

  - 结构性幻觉防控方法：生成可执行内容（如SQL、合规话术、工单模板）时，仅让LLM生成周边说明，核心可执行部分直接复用语料中的真实样本，从结构上杜绝幻觉，可直接迁移到电商售后工单生成、广告合规文案生成等场景

  - PII掩码不只是合规要求：将语料中的敏感信息替换为统一占位符，可引导模型输出通用模板而非复制历史具体值，同时避免隐私泄露，适合电商用户咨询、客服助手等场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
政务机构的敏感文档、工单数据严禁流出机构，完全无法使用云侧LLM服务，同时面临硬件预算有限（仅单台8GB消费级显卡）、系统必须只读无操作权限的强约束，亟需低成本、全本地化的RAG技术支持助手方案。

### 方法关键点
- 混合检索+意图路由：bge-m3稠密检索与罗马尼亚语稀疏全文检索经RRF融合，按query意图路由到对应语料域，SQL类查询仅检索含SQL的chunk，从检索层面降低噪声
- 8GB VRAM embedder微调方案：采用8-bit优化器+梯度检查点，解决Windows平台显存静默溢出问题，72分钟完成bge-m3全量微调；针对单域微调导致其他域检索效果下降的问题，用本地12B模型生成GenQ合成query补充多域训练数据修复效果
- 结构性幻觉防控：二阶段PII掩码替换敏感信息为占位符，SQL锚定蒸馏仅保留真实样本的可执行代码，LLM仅生成周边说明，规则拦截器提前拦截风险query，不依赖模型服从性
- 零数据流出评估：CPU侧运行744B MoE大模型做离线批量评估，替代云LLM法官，单条评估耗时约9分钟

### 关键结果
在24914个chunk（15073张历史工单+815篇规范文档）的罗马尼亚语语料上：
1. 混合检索+意图路由将内部评估得分从62%提升到81%，无任何模型微调
2. bge-m3微调后工单域recall@10从0.663提升到0.850，MRR从0.489提升到0.684；补充GenQ数据后文档域效果恢复至基线以上，工单域效果无损失
3. 全系统最终48项golden评估断言100%通过，3-bit量化12B生成模型在8GB卡上推理速度达42tok/s，硬问题平均响应延迟12.6s

### 核心启发
受限场景下大部分看似模型能力不足的问题，都可以通过系统工程修复，资源约束不会阻碍系统落地，反而会倒逼出更可靠的实现方案
