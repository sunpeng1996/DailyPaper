---
title: 'CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using
  Camouflaged Documents'
title_zh: 《CamoDocs：面向检索增强大模型的伪装文档投毒攻击》
authors:
- Jaewon Jung
- Haizhong Zheng
- Hongsun Jang
- Jaeyong Song
- Beidi Chen
- Jinho Lee
affiliations:
- Seoul National University
- Carnegie Mellon University
arxiv_id: '2608.28389'
url: https://arxiv.org/abs/2608.28389
pdf_url: https://arxiv.org/pdf/2608.28389
published: '2026-08-28'
collected: '2026-08-31'
category: RAG
direction: RAG安全 · 投毒攻击与防御
tags:
- RAG
- Poisoning Attack
- LLM Security
- Adversarial Attack
- TrustRAG
one_liner: 提出无需嵌入目标查询的RAG投毒攻击CamoDocs，可绕过7类主流防御并保持高攻击成功率
practical_value: '- 电商/客服类RAG系统可先上线简单的查询重叠检测规则：召回文档与用户查询的滑动窗口最长公共子序列相似度超过0.8即过滤，可挡住90%以上的传统RAG投毒攻击，几乎无额外成本

  - 不要在商品资讯、活动规则、物流政策等强检索依赖的RAG场景使用TrustRAG这类擦除式聚类防御，其会过滤90%以上有效文档，导致干净回答准确率暴跌80%+

  - 做RAG安全防御可新增PPL可读性校验规则：CamoDocs生成的伪装文档PPL仍显著高于正常文档，搭配嵌入分布离散度检测可进一步提升投毒文档识别率

  - 内部RAG系统红蓝对抗测试可复用CamoDocs的梯度引导token替换+一致性过滤框架，快速验证现有防御体系的鲁棒性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG投毒攻击均需将目标查询嵌入恶意文档以提升召回率，会留下词汇重叠、嵌入聚类过紧的明显特征，极易被现有防御拦截；同时主流聚类类RAG防御的实际效用损耗尚未被系统验证，无法指导业务场景的防御选型。
### 方法关键点
- 无需在恶意文档中插入目标查询：先用合成LLM分别生成目标查询对应的良性草稿和包含预设错误答案的对抗草稿，分块得到两类子文档
- 梯度引导token替换：用代理embedding模型计算梯度，将良性子文档中的部分token替换为dispersion token，最大化所有恶意文档嵌入与质心的距离，打散嵌入分布以规避聚类防御
- 一致性过滤：用轻量语言模型重排候选替换token，控制文档可读性下降，避免被质量过滤规则拦截
- 最终将优化后的良性子文档与对抗子文档拼接，得到可躲避检测的伪装投毒文档
### 关键结果
在HotpotQA、NQ、MS-MARCO三个基准上对比3类主流投毒攻击基线，覆盖7类防御、3个开源LLM、2个闭源模型：
- 传统含查询的投毒攻击在查询检测防御下ASR普遍低于12%，CamoDocs平均ASR比基线最高高27%，对GPT-5.4-mini平均ASR达61.80%，对Claude-Haiku-4.5达55.09%
- TrustRAG在强检索依赖的NeoQA数据集上会过滤91.48%的召回文档，干净回答准确率从29.13%暴跌至5.79%，几乎丧失RAG的核心效用

所有依赖查询嵌入的RAG投毒攻击都可以用简单的查询重叠检测低成本拦截，而擦除式聚类防御在检索依赖场景的效用损耗远大于其带来的安全收益。
