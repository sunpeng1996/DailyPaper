---
title: Diffusion Language Models for Perplexity-Aware Black-Box Attacks
title_zh: 基于扩散语言模型的困惑度感知黑盒攻击方法
authors:
- Ali Al-Lawati
- Elsayed Eshra
- Dongwon Lee
- Suhang Wang
affiliations:
- The Pennsylvania State University
arxiv_id: '2610.31558'
url: https://arxiv.org/abs/2610.31558
pdf_url: https://arxiv.org/pdf/2610.31558
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: 大语言模型 · 黑盒对抗攻击
tags:
- Diffusion Language Model
- Black-box Attack
- Adversarial Prompt
- Perplexity
- LLM Safety
one_liner: 将扩散语言模型接入连续空间攻击框架，生成低困惑度、难检测的黑盒LLM对抗提示
practical_value: '- 做LLM Agent/电商智能客服的安全防护时，可复用本方法生成低PPL对抗样本，测试输入 guardrails 检测能力

  - 构建电商UGC（评论/咨询）、搜索query风控模型时，可生成该类自然度高的对抗样本做负样本增强，提升风控召回率

  - 面向电商场景的LLM做对齐微调时，可引入本方法生成的对抗样本作为负例，提升模型抗prompt注入攻击的鲁棒性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有黑盒LLM连续空间攻击依赖随机映射生成对抗提示，自然度极低，易被输入防护规则拦截，得到的风险评估结果不符合真实自然prompt场景。
### 方法关键点
将连续扩散语言模型（dLLM）接入原有连续空间攻击框架，替换原有的随机映射+最近token查找模块，保留标准高斯隐空间定义与下游采样/优化流程，分别在采样式评估（RareTrap）、优化式搜索（ThinkTrap）两种攻击范式下验证效果。
### 关键结果
- RareTrap场景下字符级perplexity从10³~10⁷降至3~5
- ThinkTrap场景下字符级perplexity从20~28降至4.3~5.4
- 不同映射方式得到的模型风险评估结果差异可达1个数量级
