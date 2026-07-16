---
title: 'The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance,
  Distortion and a Validation Protocol'
title_zh: 合成大模型裁判语料的测试预言机问题：失效、失真与验证协议
authors:
- Serkan Ballı
affiliations:
- Department of Software Engineering, Mehmet Akif Ersoy University, Türkiye
arxiv_id: '2607.13707'
url: https://arxiv.org/abs/2607.13707
pdf_url: https://arxiv.org/pdf/2607.13707
published: '2026-07-15'
collected: '2026-07-16'
category: Eval
direction: 大模型自动裁判 · 评测语料验证
tags:
- LLM-as-Judge
- Evaluation Corpus
- Test Oracle
- Synthetic Data
- Multilingual Evaluation
one_liner: 揭示合成LLM-as-Judge语料的结构性构造缺陷，给出无预言机场景下的验证流程
practical_value: '- 做LLM-as-Judge自动化评测（如推荐文案质量、Agent回答效果打分）时，优先用黄金答案确定性扰动构造负例，可通过字符串比对100%校验样本完整性

  - 若必须用生成式负例构造评测语料，不要复用生成和裁判步骤的解码参数（如max tokens），避免样本截断引入虚假评测偏差

  - 评测结果出现异常波动（如跨语言效果骤降、偏差方向反转）时，优先抽查原始生成样本完整性，聚合统计指标无法识别这类构造缺陷'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM-as-Judge偏差研究普遍采用大模型生成幻觉答案作为负例构造合成语料，该构造模式存在结构性失效风险，且常规聚合统计校验无法识别。
### 方法关键点
基于多语言（土耳其语/英语）忠实度评测语料开展对照实验，定位生成与裁判步骤共享解码预算导致的样本截断问题，对比生成式负例、确定性扰动负例两类语料的容错能力，推导无预言机场景的验证协议。
### 关键结果
参数错误导致单裁判跨语言选择准确率出现32pp的虚假暴跌，修正参数后效果直接达到天花板；确定性扰动构造的语料可通过零成本字符串比对100%识别同类故障，聚合统计指标完全无法检测生成式语料的样本缺陷。
