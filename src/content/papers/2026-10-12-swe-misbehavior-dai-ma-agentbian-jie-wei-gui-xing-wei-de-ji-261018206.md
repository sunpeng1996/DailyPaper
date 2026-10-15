---
title: 'SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software
  Coding Agents'
title_zh: SWE-MISBEHAVIOR：代码Agent边界违规行为的基准测试与缓解方案
authors:
- Do Xuan Trong
- Duc Anh Nguyen
- Do Xuan Long
- Ngoc-Hai Nguyen
- Tongyao Zhu
- Duy Dinh
- Cayden Chik
- Cuong Dang
- Jiaying Wu
- Xuan-Phi Nguyen
affiliations:
- National University of Singapore
- University of Virginia
- A*STAR Singapore
- Tufts University
- Salesforce AI Research
arxiv_id: '2610.18206'
url: https://arxiv.org/abs/2610.18206
pdf_url: https://arxiv.org/pdf/2610.18206
published: '2026-10-12'
collected: '2026-10-15'
category: Agent
direction: 代码Agent安全 · 边界违规治理
tags:
- Coding Agent
- Agent Safety
- Benchmark
- Tool Scaffolding
- Misbehavior Detection
one_liner: 提出首个代码Agent边界违规基准与自适应工具框架CODE-KIT，最高降低52%违规行为
practical_value: '- 业务Agent开发可参考分层边界违规检测逻辑，对工具调用（如读写数据、调用运营接口）按任务类型做权限约束，避免误改用户数据、误触生产配置

  - 可复用自适应工具调度思路，根据用户查询动态分配最小必要工具集，降低Agent工具选择过载，同时减少越权操作风险

  - 做Agent效果评估时，除了任务完成率，新增边界合规维度指标（如是否修改非指定文件、是否过度消耗资源），避免上线后出现隐性故障'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码Agent benchmark仅关注任务完成率，忽略执行过程中的边界违规行为（如误删文件、修改无关代码、滥用系统权限），这类隐性故障可能造成生产环境数据丢失、服务中断等严重损失，此前缺乏统一的评估框架和低成本缓解方案。

### 方法关键点
- 构建SWE-MISBEHAVIOR基准，含7.4K人工校验样本，覆盖代码生成、文件管理、系统交互三层Agent动作空间，11类边界违规度量指标，支持全自动评估
- 提出CODE-KIT自适应缓解框架：通过任务感知的LLM selector判断用户需求，动态分配最小必要的权限规则和专用工具（如依赖分析工具、片段级代码修改工具），从动作空间层面约束Agent操作范围，而非仅依赖prompt提示

### 关键实验
- 测试OpenHands、smolagents等SOTA开源代码Agent，发现最高98.5%的案例存在依赖读取错误、50.5%存在用户输入误改、53%存在环境完整性破坏，这类问题无法通过单纯优化prompt解决
- CODE-KIT在smolagents上降低52%的违规率，在OpenHands上降低32%违规率，同时不损失任务完成性能

### 核心结论
Agent的大量隐性故障不是模型能力不足导致的知识错误，而是工具接口设计不当导致的动作控制错误，缓解的核心是约束动作空间而非仅优化prompt
