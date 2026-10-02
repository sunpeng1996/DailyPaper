---
title: 'Rules to Tools: Executable Checks for LLM Agents in Scientific Computing'
title_zh: Rules to Tools：面向科学计算LLM Agent的可执行检查框架
authors:
- Jingjie Ning
- Guojiang Zhao
- Chen Xu
- Shanshan Zhong
- Xiaochuan Li
- Ji Zeng
- Guolin Ke
affiliations:
- Carnegie Mellon University
- DP Technology
arxiv_id: '2610.00313'
url: https://arxiv.org/abs/2610.00313
pdf_url: https://arxiv.org/pdf/2610.00313
published: '2026-09-28'
collected: '2026-10-02'
category: Agent
direction: Agent 代码生成与自修复工具设计
tags:
- LLM Agent
- Code Generation
- Self-Correction
- Executable Check
- Scientific Computing
one_liner: 将公开科学计算需求封装为可调用检查工具，提升LLM Agent代码修复成功率与迭代效率
practical_value: '- 搭建Agent自修复链路时，可将业务规则（如推荐合规要求、广告投放约束、电商权益发放规则等）封装为预定义可调用检查工具，替代让LLM自行构造校验逻辑，可降低校验错误率同时减少token消耗

  - 工具交付形式不影响最终效果：封装为专用命令或直接提供Python源码均可达到相同收益，工程实现可根据现有架构灵活选择

  - 可将校验工具对初始版本的检查报告作为Agent的输入，能在不损失效果的前提下减少迭代步数，适合实时性要求高的Agent链路'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前科学计算类LLM Agent编写代码后，往往需要自行实现校验逻辑验证结果是否符合物理定律、数学约束，不仅消耗大量token，还容易因校验逻辑错误导致代码问题漏判，最终修复成功率低。

### 方法关键点
- 提出Rules to Tools (R2T) 框架，将公开科学计算需求（如边界值约束、物理守恒定律、方程残差要求等）封装为与文字描述完全等价的可调用检查工具，Agent可直接调用获取结构化校验结果
- 严格控制对照实验变量：对照组仅拿到文字版规则、自行实现校验逻辑，实验组额外拿到预构建检查工具，两组的模型、初始代码、计算预算完全一致
- 支持多种工具交付形式：专用命令、Python源码、初始检查报告等，可灵活适配不同Agent架构

### 关键实验结果
在SciCode、PDEAgentBench等4个科学计算基准上测试，核心结果：
1. 两个SciCode任务队列，对照组修复成功率26/30，实验组29/30，相对提升11.5%
2. PDE任务上实验组修复成功率24/24，对照组23/24，同时模型输出token减少31.2%
3. 开发暴露任务集上，对照组修复成功率3/10，实验组7/10，相对提升133%
4. 效果提升的tradeoff为工具组公共CPU消耗平均提升87.3%

### 核心结论
将业务规则预实现为可调用的校验工具，比让LLM读取规则后自行编写校验逻辑，效果更好、整体成本更低
