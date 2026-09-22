---
title: 'Decoding Guardrails: XAI-Guided Perturbation Analysis of Prompt Injection
  Detection'
title_zh: 解析安全护栏：XAI引导的提示词注入检测扰动分析
authors:
- Fernando Outeda
- Gustavo Betarte
- Juan Diego Campo
- Fiorella Cravero
affiliations:
- Pedeciba Informática, Uruguay
- InCo, Facultad de Ingeniería, Universidad de la República
- Departamento de Informática e Inteligencia Artificial, Universidad Católica del
  Uruguay
arxiv_id: '2609.24801'
url: https://arxiv.org/abs/2609.24801
pdf_url: https://arxiv.org/pdf/2609.24801
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM安全 · 提示注入检测
tags:
- LLM
- Prompt Injection
- XAI
- Guardrails
- Adversarial Robustness
one_liner: 用XAI技术分析Prompt Guard 2提示注入检测逻辑，揭示其脆弱性与低成本对抗绕过路径
practical_value: '- 电商Agent/LLM服务部署时，提示注入检测不能仅依赖词法特征，需补充语义级校验逻辑，规避同义替换/paraphrase绕过风险

  - 可复用Vanilla Gradient、SHAP等XAI归因方法，用于自检自研prompt防护策略的鲁棒性，提前暴露检测逻辑漏洞

  - 训练自研prompt注入检测模型时，可引入saliency引导的对抗样本做数据增强，大幅提升模型抗绕过能力'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
LLM在生产系统大规模部署中面临严重的prompt注入、越狱攻击风险，当前主流的分类器式防护护栏（如Prompt Guard 2）决策逻辑高度黑盒，攻防双方均对其检测机制缺乏明确认知。
### 方法关键点
采用Vanilla Gradient、SHAP两类XAI归因方法引导扰动分析，开展4组实证实验，从token级归因、对抗扰动测试、数据集级显著性分析三个维度拆解Prompt Guard 2的检测逻辑。
### 关键结果
1. Prompt Guard 2的决策依赖多token累积贡献，而非少数核心token；
2. 仅修改中等比例文本的显著性引导同义替换、句子级paraphrase即可翻转检测结果，部分样本可成功越狱底层LLM；
3. 未被检测的注入prompt普遍缺少分类器依赖的词法标记，现有护栏鲁棒性不足。
