---
title: 'Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities
  Invisible to Standard Evaluation'
title_zh: 微调如何产生标准评估无法检测的LLM规避漏洞
authors:
- Ryan Fetterman
affiliations:
- Cisco Talos
arxiv_id: '2606.27091'
url: https://arxiv.org/abs/2606.27091
pdf_url: https://arxiv.org/pdf/2606.27091
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM微调安全 · 规避漏洞检测
tags:
- Fine-tuning
- Evasion Vulnerability
- Security LLM
- Linear Probe
- Model Drift
one_liner: 揭示安全分类LLM微调继承基础模型电路生成脆弱规则，提出部署前漂移检测方法
practical_value: '- 做垂域LLM微调（比如电商合规审核、广告反作弊分类器）时，不能仅测同分布holdout集，必须补充行为等价变换样本（同义词替换、语序调整、大小写变体等）测试鲁棒性

  - 微调后可复用文中的线性探针+指示词符号检验方法，低成本检测微调导致的语义漂移，提前发现模型脆弱的特征依赖规则

  - 做Agent工具调用安全校验时，避免仅依赖特定token做分类判断，需针对指令的等价变换空间做全链路覆盖，防止恶意prompt绕过校验'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有垂域分类LLM微调后仅采用同分布留出集评估，会遗漏微调本身引入的规避漏洞：模型学习到的token级指示符特征仅在标准样本上保持准确率，在行为等价变换下完全失效。

### 方法关键点
以Llama-3.1-8B-Instruct及其微调得到的安全分类模型Foundation-Sec-8B-Instruct为研究对象，通过因果干预定位分类电路来源于基础模型的后期注意力通路，微调仅强化该通路与特定命令指示符的关联；提出结合基础模型激活线性探针、指示词符号检验的部署前监测方法，可低成本识别微调后语义漂移的命令族，指导测试用例生成。

### 关键结果
三级规避基准测试显示，微调后的Foundation-Sec在iwr别名替换、Invoke-Expression重构、大小写变体三类变换下的漏判率显著高于基础Llama模型，同分布评估准确率可达标但完全无法发现这类脆弱点。
