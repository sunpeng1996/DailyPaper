---
title: 'TDD-Agent: Test-Driven Reasoning for Code Generation'
title_zh: TDD-Agent：基于测试驱动推理的代码生成框架
authors:
- Hongyue Yu
- Kefan Li
- Jiakun Li
- Hongzheng Chai
- Yuan Yuan
- Rui He
- Junyi Wei
affiliations:
- Beihang University
- Beihang University Qingdao Research Institute
- Beihang University Hangzhou Innovation Institute
arxiv_id: '2608.16742'
url: https://arxiv.org/abs/2608.16742
pdf_url: https://arxiv.org/pdf/2608.16742
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 代码生成Agent · 测试驱动开发
tags:
- Code Generation
- Test-Driven Development
- LLM Agent
- Iterative Refinement
- Repository-Level Coding
one_liner: 将测试驱动开发范式落地为单Agent代码生成框架，双轨迭代优化代码与测试
practical_value: '- 电商生成式推荐/文案生成场景可复用测试先行思路：先定义可执行的校验用例（如推荐品匹配度、文案合规性、优惠信息正确性规则）再生成内容，从源头降低LLM幻觉

  - Agent迭代流程可复用双轨优化设计：不仅迭代生成的业务结果，同时迭代校验规则本身，避免规则缺陷导致的误判、漏判，提升整体输出准确率

  - 资源受限场景可参考迭代次数权衡结论：6-7轮迭代后效果收益边际递减，可根据业务对时延、算力的要求选择迭代轮次，平衡投入产出比

  - 单Agent即可模拟开发+测试双角色，无需多Agent调度开销，适合中小业务快速落地类Agent需求，降低架构复杂度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM代码生成方案大多将生成的测试作为事后静态校验工具，存在两个核心缺陷：一是测试本身的错误或不完整会引入误导性反馈，二是仅支持函数级简单任务，无法适配仓库级复杂代码生成场景，代码正确率提升天花板明显。
### 方法关键点
- 两阶段核心工作流：第一阶段先让Agent生成目标功能的单元测试，强制明确输入输出、边界条件等预期行为后再编写实现代码；
- 双轨迭代优化机制：测试和代码均为可变对象，根据测试执行反馈同时迭代两者，支持Agent判断任务完成后提前终止，最大迭代轮次默认为10；
- 轻量工具集支撑：内置目录查看、代码结构解析、代码搜索、测试执行等工具，单Agent即可完成全流程，无需多Agent协作的调度开销。
### 关键结果
函数级任务在LiveCodeBench评测，TDD-prompt相比CoT、Self-Planning等基线，在GPT、DeepSeek、Qwen三个模型上均取得最优Pass@1，最高提升2.63个百分点；仓库级任务在RepoEval评测，10轮迭代的TDD-Agent相比mini-SWE-agent基线，在三个模型上分别提升16.93%、6.59%、6.37%的Pass率；迭代6-7轮后效果收益趋近饱和，错误归因（分不清是代码错还是测试错）的问题占比不超过10%。

生成的测试不应被当作固定校验器，而是可以和生成结果共同迭代的推理辅助载体。
