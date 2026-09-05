---
title: 'PatchBench: Evaluating AI Agents for Vulnerability Patching'
title_zh: PatchBench：面向漏洞修复的AI Agent评估基准
authors:
- Chihao Shen
- Jiacheng Li
- Aastha Mahajan
- Jeffery Siyuan Tian
- Yonghwi Kwon
- Yizheng Chen
affiliations:
- University of Maryland
arxiv_id: '2609.04075'
url: https://arxiv.org/abs/2609.04075
pdf_url: https://arxiv.org/pdf/2609.04075
published: '2026-09-03'
collected: '2026-09-05'
category: Agent
direction: Agent 垂直任务效果评估基准
tags:
- Agent Evaluation
- Vulnerability Patching
- Benchmark
- LLM Agent
- Validation Method
one_liner: 提出漏洞修复Agent评估基准PatchBench，解决现有评估记忆作弊、表层修复漏判问题
practical_value: '- 做Agent效果评估时可参考其防作弊思路：通过任务上下文迁移、规则扰动规避模型靠记忆训练集数据刷指标的问题

  - 评估任务完成度不能只看表层输出达标，要新增根因校验逻辑，避免模型生成仅符合表层规则的无效输出

  - 可复用其相似度匹配检测方案，识别LLM生成内容是否照搬训练集样本，规避业务合规风险'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AI Agent漏洞修复评估仅验证PoC输入是否还触发崩溃，存在两大有效性缺陷：一是Agent可能输出记忆的历史补丁，二是仅生成压制崩溃的表层修复，未解决问题根因，评估结果虚高。

### 方法关键点
1. 设计补丁相似度指标，可检测模型输出的记忆类补丁
2. 构建PatchBench基准：筛选真实修复逻辑在崩溃栈外的漏洞，通过漏洞移植、代码突变将历史漏洞迁移到新代码上下文，从数据源层面规避表层修复、记忆作弊问题
3. 新增补丁安全性、语义正确性双重校验逻辑，替代原有仅靠PoC的单维度校验

### 关键结果数字
平均25%的Agent生成补丁与历史开发者补丁高度相似；原有仅靠PoC的评估方式会把11个SOTA Agent的修复成功率平均高估1.83倍
