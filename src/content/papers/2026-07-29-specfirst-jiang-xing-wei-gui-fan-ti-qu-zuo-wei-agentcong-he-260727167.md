---
title: 'SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based
  Program Synthesis from Scratch'
title_zh: SpecFirst：将行为规范提取作为Agent从零合成程序的前置核心步骤
authors:
- Yihao Chen
- Shi Chang
- Feng Lin
- Khaled Chawa
- Boyuan Chen
- Shaowei Wang
- Ahmed E. Hassan
affiliations:
- Huawei Canada
- Queen's University
- University of Manitoba
- Concordia University
arxiv_id: '2607.27167'
url: https://arxiv.org/abs/2607.27167
pdf_url: https://arxiv.org/pdf/2607.27167
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: Agent程序合成 · 任务分阶段解耦
tags:
- LLM Agent
- Program Synthesis
- Specification Elicitation
- ReAct
- ProgramBench
one_liner: 提出两阶段Agent程序合成框架，先提取结构化行为规范再编码，大幅提升从零复现程序的准确率
practical_value: '- 做复杂Agent任务时可复用「需求提取+执行」两阶段解耦架构：比如电商Agent搭建活动页、生成推荐规则时，先让专门的需求Agent对齐业务边界、边缘案例、错误场景，输出结构化Spec再执行，避免边做边改浪费token和时间

  - 可复用Spec Agent的四类探测策略：边界探测、错误路径触发、组合条件测试、输出格式校准，在搜索Query意图对齐、广告文案合规检测等场景下，用来系统梳理业务规则的覆盖场景，减少遗漏

  - 多Agent间信息传递可固定使用6段式Spec模板（概述/参数/输入/输出/错误/边案例），实测比自由格式、正式规范格式的下游执行准确率更高，适合作为标准化协作接口

  - 长周期Agent任务中把核心规则固化为外部结构化文件，可解决上下文漂移、早期错误传播问题：比如推荐系统规则生成Agent迭代时，用固定Spec锚定核心约束，避免多轮迭代后偏离初始需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于LLM的代码Agent在从零复现程序任务上表现极差，前沿模型在ProgramBench基准上全量通过率不足1%。核心问题是现有框架将需求理解、行为探测、代码合成混在单循环中，导致三个系统性缺陷：探测不充分遗漏文档未提及的边缘案例、长上下文下需求漂移、早期错误无锚点持续传播。传统软件工程中需求提取作为前置核心阶段的实践可有效解决上述问题。

### 方法关键点
- 两阶段解耦架构：第一阶段由专门的Spec Agent负责黑盒探测目标程序，输出结构化行为规范SPEC.md；第二阶段代码合成Agent基于SPEC.md完成实现，可直接复用SWE-agent等现有代码Agent能力
- Spec Agent四类定向探测策略：边界探测（极限输入测试）、错误路径触发（异常输入测试）、组合参数测试（多参数交互测试）、输出格式校准（细节对齐测试），覆盖文档遗漏的行为细节
- 结构化Spec固定采用6段式模板：概述、参数、输入、输出格式、错误模式、边缘案例，平衡结构化程度和灵活性，实测比自由格式、OpenSpec格式的下游执行准确率更高
- 上下文管理：仅将SPEC.md传递给代码合成Agent，丢弃Spec Agent的推理过程等冗余信息，避免上下文过载

### 关键实验结果
在ProgramBench全200个真实开源工具实例上测试，跨4个不同能力、不同家族的模型，对比单循环基线：测试通过率提升6.9%~21.3%，其中硬难度任务最高提升29.9%，90%以上测试通过率的实例占比从5.5%提升到16.5%；二进制探测覆盖率提升9.4%~18.5%，覆盖提升完全来自Spec Agent的前置探测阶段；代码合成Agent提前进入编码阶段，最终代码量提升7%~29%，减少无效探测消耗的轮次。

**最值得记住的结论**：把需求提取作为Agent复杂任务的前置第一阶段，是提升任务准确率、减少错误传播的通用有效范式。
