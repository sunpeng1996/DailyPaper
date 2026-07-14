---
title: 'PTEI: Integrating Personality Traits to Enhance Emotional Intelligence in
  Large Language Models'
title_zh: PTEI：融合人格特质提升大语言模型的情绪智力能力
authors:
- Amir Reza Jafari
- Praboda Rajapaksha
- Reza Farahbakhsh
- Noel Crespi
affiliations:
- Samovar, Telecom SudParis, Institut Polytechnique de Paris
- Department of Computer Science, Aberystwyth University
arxiv_id: '2607.10245'
url: https://arxiv.org/abs/2607.10245
pdf_url: https://arxiv.org/pdf/2607.10245
published: '2026-07-11'
collected: '2026-07-14'
category: LLM
direction: 大语言模型 · 情绪推理能力优化
tags:
- LLM
- Emotional Intelligence
- Personality Traits
- Contrastive Learning
- Chain-of-Thought
one_liner: 提出融合MBTI、OCEAN人格特质的PTEI框架，提升大语言模型情绪理解与推理能力
practical_value: '- 电商客服Agent可引入MBTI/OCEAN人格识别模块，从用户交互内容提取人格特征后定制回复话术，提升用户情绪满意度

  - 个性化推荐场景可复用「场景特征提取+对比学习构建对齐召回池」的架构，优化用户偏好匹配精准度

  - LLM调用流程中可在prompt注入人格感知上下文，搭配CoT推理，可提升情绪类任务准确率约4%'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前LLM在复杂情绪推理任务上表现远逊于人类，核心差距来源之一是未纳入人格特质这类人类情绪推断依赖的核心个体差异要素。
### 方法关键点
1. 提出PTEI框架，先从输入的情绪场景中直接提取MBTI、OCEAN两类人格特质，作为上下文注入人格感知prompt，引导LLM准确推断情绪及背后成因
2. 采用对比学习构建优化检索系统，召回情绪、人格对齐的相似场景，增强推理的上下文grounding效果
### 关键结果
在标准EI基准测试中，PTEI可提升各类LLM的情绪理解能力，其中GPT系列模型增益最显著；搭配CoT推理可额外获得4%的准确率提升。
