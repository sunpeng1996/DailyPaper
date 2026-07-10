---
title: 'Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions'
title_zh: 警惕自动补全风险：带后门代码补全的溯源归因
authors:
- Anjun Gao
- Yueyang Quan
- Zhuqing Liu
- Minghong Fang
affiliations:
- University of Louisville
- University of North Texas
arxiv_id: '2607.08011'
url: https://arxiv.org/abs/2607.08011
pdf_url: https://arxiv.org/pdf/2607.08011
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM安全 · 后门攻击溯源
tags:
- Backdoor Attack
- Code Completion
- Forensic Attribution
- LLM Security
- Fine-tuning Poisoning
one_liner: 提出CodeTracer框架，仅需微调语料和异常补全事件即可溯源代码补全模型的后门投毒数据
practical_value: '- 代码生成类Agent可复用该「结构化行为指纹提取+语义检索+LLM推理」链路，排查恶意生成内容的训练数据来源

  - 大模型微调数据投毒检测场景可借鉴该「问题样本→语义匹配候选数据→归因判断」的三段式框架，降低误判率

  - 电商场景下智能客服、商品文案生成等LLM应用的风险溯源，可参考该方法在仅依赖微调语料的约束下实现问题定位'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前基于LLM的代码补全系统易遭受后门投毒攻击，恶意微调数据会植入不安全行为，现有防御方案难以应对自适应复杂攻击，且部署后无法快速溯源恶意生成对应的问题训练数据。
### 方法关键点
提出CodeTracer取证框架，仅依赖微调语料和上报的错误补全事件运行：1）从恶意输出中提取结构化行为指纹；2）通过语义检索缩小候选代码样本范围；3）基于LLM推理将不安全逻辑归因到具体的后门微调数据。
### 关键结果
在3类典型漏洞场景、10种后门攻击、16个竞争基线的对比测试中，CodeTracer始终保持高取证准确率、低误识别率，对自适应攻击具备强鲁棒性。
