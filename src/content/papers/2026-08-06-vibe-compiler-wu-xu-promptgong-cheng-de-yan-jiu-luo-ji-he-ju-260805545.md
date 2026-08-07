---
title: 'Vibe Compiler: A Research-Logic Synthesis Tool That Runs without Prompt Engineering
  -Toward Enhancing Metacognition for Sustaining Agency in the Age of Generative AI-'
title_zh: Vibe Compiler：无需Prompt工程的研究逻辑合成工具
authors:
- Riichiro Mizoguchi
- Tomoki Aburatani
- Kento Koike
- Machi Shimmei
affiliations:
- Japan Advanced Institute of Science and Technology
- Osaka Metropolitan University
- Kanagawa University
- Tohoku University
arxiv_id: '2608.05545'
url: https://arxiv.org/abs/2608.05545
pdf_url: https://arxiv.org/pdf/2608.05545
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 人机协作 · 元认知增强
tags:
- Human-AI Collaboration
- Metacognition
- Epistemic Agency
- Synthesis-Analysis Reciprocity
- Ontology
one_liner: 基于合成-分析互惠模型，打造引导人类元认知、保留认知主体性的AI辅助研究工具
practical_value: '- 可复用「AI合成+AI自检输出逻辑缺口→引导人类决策」的人机协作框架，替代AI直接输出结果的模式，降低推荐/广告策略生成中的认知卸载风险，保留业务人员决策主体性

  - 无需复杂Prompt工程，通过给LLM喂入领域结构化Ontology（如电商场景的业务规则、指标体系）即可实现标准化逻辑校验，降低Prompt维护成本，提升AI输出合规性

  - 可借鉴四类结构缺口归因框架，拆解人机协作各环节的责任归属，解决推荐/广告系统迭代中AI生成结果的责任边界模糊问题'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
生成式AI普及大幅提升了知识生产效率，但也导致人类被动接受AI输出、认知卸载严重，逐渐丧失认知主体性与批判性思考能力。现有AI辅助工具要么以效率为核心直接输出完整结果，要么依赖人类主观反思缺乏客观校验机制，无法在AI协作过程中保留并驱动人类元认知提升。
### 方法关键点
- 提出合成-分析（S&A）互惠模型，将知识构建拆解为Synthesis（选择组合逻辑组件生成输出）、Analysis（基于客观指标校验输出）的双向约束循环，Analysis的结果直接作为下一轮Synthesis的输入约束
- 从执行主体（人/AI）、认知功能（Synthesis/Analysis）两个正交维度划分四类协作模式，采用「AI主导合成+AI主导分析，仅输出逻辑缺口引导人类判断」的设计，将AI定位为批判性校验工具而非直接输出答案的助手
- 基于包含16个学术参数的论文Ontology开发Vibe Compiler原型，检测到逻辑缺失时不自动补全，而是输出反思问题引导人类自行完善逻辑
### 关键结果
基于NotebookLM和Gemini构建的原型无需Prompt工程，仅喂入7类非形式化的结构化领域文档即可稳定运行，成功支撑了本篇论文的完整逻辑构建，验证了研究者层的可用性；双分层设计可直接扩展到学习者层（数学出题、阅读理解等场景），仅需替换Analysis的领域指标即可适配不同场景。
### 核心结论
生成式AI辅助系统的核心价值不应是替人类完成工作，而是通过暴露主观认知与客观结构的缺口驱动人类元认知提升，让人类从AI输出的执行者升级为掌握决策权的管理者。
