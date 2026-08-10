---
title: 'Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits'
title_zh: 扩散大语言模型作为攻击目标与对手的机制性安全漏洞研究
authors:
- Elena Dumitrescu
- Gert Lek
- Lydia Y. Chen
- Jérémie Decouchant
affiliations:
- Delft University of Technology
- University of Neuchâtel
arxiv_id: '2608.07430'
url: https://arxiv.org/abs/2608.07430
pdf_url: https://arxiv.org/pdf/2608.07430
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: 扩散大语言模型 · 安全对齐漏洞挖掘
tags:
- Diffusion LLM
- Safety Alignment
- Jailbreak
- Transfer Attack
- Mechanistic Interpretability
one_liner: 揭示扩散大语言模型安全对齐的可迁移漏洞，提出低成本离线黑盒越狱框架SN-Guided Diffusion
practical_value: '- 部署电商/客服/内容生成Agent时，可参考安全神经元映射方法快速定位DLLM的安全薄弱单元，针对性加固降低越狱风险

  - SN-Guided Diffusion的低代价黑盒测试思路可复用在业务LLM服务的红蓝对抗中，以极低的成本完成批量安全巡检

  - 跨架构安全特征可迁移的结论提示：基于开源预训练LLM二次开发业务模型时，需补充专属对齐训练覆盖上游遗留的安全漏洞'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Diffusion LLM（DLLM）以并行迭代去噪替代自回归生成，但内部安全对齐机制的漏洞特征与跨架构迁移性尚不明确，缺乏低成本的安全测试方案。
### 方法关键点
1. 验证DLLM安全对齐神经元具备稀疏性与跨架构可迁移性：自回归预训练源模型的安全特征会被派生DLLM直接继承，可通过安全神经元映射、剪枝实现跨架构迁移攻击；
2. 提出SN-Guided Diffusion全离线黑盒越狱框架，通过加权安全神经元损失引导扩散过程避开安全触发区域。
### 关键结果数字
自剪枝攻击将LLaDA攻击成功率（ASR）从2.6%提升至73.8%，Dream ASR从1.9%提升至86.6%；跨模型迁移剪枝将Fast-dLLM ASR从7.0%提升至86.3%；新框架对Llama-3-8B-Instruct、Qwen2.5-7B-Instruct、Gemini-2.5-Flash-Lite的迁移ASR分别达77.1%、86.9%、74.3%，仅需每prompt 20次生成，成本较传统方案低数个数量级，良性/越狱prompt区分AUROC达1.0。
