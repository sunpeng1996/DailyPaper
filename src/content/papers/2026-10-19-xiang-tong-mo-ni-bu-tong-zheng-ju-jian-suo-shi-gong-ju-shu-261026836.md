---
title: 'Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM
  Agents Accuracy'
title_zh: 相同模拟不同证据：检索式工具输出如何降低LLM Agent准确率
authors:
- Ke Zhang
- Sahchit Chundur
- Jerry Peprah Owusu
- Mohammad Javad Abdolhosseini Qomi
- Maziar Raissi
affiliations:
- University of California, Riverside
- University of California, Irvine
arxiv_id: '2610.26836'
url: https://arxiv.org/abs/2610.26836
pdf_url: https://arxiv.org/pdf/2610.26836
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: LLM Agent 工具调用上下文管理优化
tags:
- LLM Agent
- Tool Calling
- Context Management
- Retrieval
- Failure Attribution
one_liner: 定位LLM Agent工具输出检索的证据替换错误，提出低成本准确率提升方案
practical_value: '- 工具调用类Agent框架设计时，明确指定权威输出文件（如接口返回、爬取原页面）的优先级，禁止优先读取Agent自身生成的中间缓存文件，可大幅降低数值计算、精确匹配类任务的错误率

  - 针对电商场景的工具类推荐Agent（比价、库存查询、优惠券核销Agent等），优先inline长度适配的工具输出，长输出搭配检索读取，可在控制token成本的同时避免精度损失

  - Agent性能评估不能仅看最终准确率，需拆解为工具调用是否正确、正确结果是否被读取、读取后是否正确使用三个环节，避免因工具成功率提升掩盖证据使用环节的隐性损失

  - 不要单独给Agent加「正确四舍五入」类格式化提示，直接指定从权威输出读取已格式化的结果，投入产出比更高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent处理长工具输出时普遍采用「存为文件+按需检索」的模式降低context占用，但已有研究发现该模式会无差别降低准确率，却未定位损失发生的具体环节，难以针对性优化。

### 方法关键点
- 基于确定性地学模拟器PHREEQC设计158道经重跑验证的数值类选择题，所有答案可溯源，排除工具本身不确定性干扰
- 仅改变工具输出的交付方式：inline（直接塞入context）、TOC（仅返回目录，Agent按需检索读取）、Grep（仅返回元数据，Agent正则搜索读取）三种模式
- 把Agent准确率拆解为3个可观测环节：Build（模拟是否生成正确结果）、Exposure（正确结果是否被Agent读取到）、Closure（读取后是否正确回答）

### 关键实验
- 数据集为158道PHREEQC仿真选择题，以inline模式为baseline，TOC检索模式下GPT-5.1准确率降11.3pp，GPT-5.2降7.9pp，Claude系列无明显损失；GPT-5.4净准确率无变化，但证据使用环节隐性损失约10pp，被更高的工具调用成功率掩盖
- 干预实验：给Agent增加「必须从模拟器主报告取答案」的提示，三个GPT模型准确率提升6.3~7.9pp；仅增加「正确四舍五入」提示无明显效果；短输出直接inline的混合模式效果与加提示相当

### 最值得记住的一句话
Agent上下文管理策略的优劣不能仅用最终准确率判断，要定位到证据获取、使用的具体环节，避免隐性损失
