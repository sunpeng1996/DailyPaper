---
title: 'Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code'
title_zh: 生成式编译：AI代码生成过程中的实时编译器反馈
authors:
- Niels Mündler-Sasahara
- Hristo Venev
- Dawn Song
- Martin Vechev
- Jingxuan He
affiliations:
- ETH Zurich
- INSAIT
- Sofia University "St. Kliment Ohridski"
- University of California, Berkeley
arxiv_id: '2607.13921'
url: https://arxiv.org/abs/2607.13921
pdf_url: https://arxiv.org/pdf/2607.13921
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: LLM代码生成实时反馈优化
tags:
- LLM
- Code Generation
- Compiler Feedback
- Constrained Decoding
- Rust
one_liner: 提出基于Sealor转换的生成式编译框架，在LLM代码生成过程中实时引入编译器反馈降低错误率
practical_value: '- 开发代码生成类Agent（如电商内部自动化运维、数据处理脚本生成Agent）时，可借鉴Sealor转换思路，将不完整的中间生成内容转换为合规可校验格式，提前引入规则校验反馈，减少错误级联

  - 无LLM白盒访问权限的约束生成场景，可复用「中间输出补全+现有校验工具实时反馈」的架构，避免重实现语义约束的高昂成本

  - 生成式推荐、广告文案生成场景中，可参考该思路，将不完整的生成候选提前补全后送入合规校验（如敏感词、广告法规则校验），提前拦截无效生成，降低后处理成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Rust等静态语义严格的语言可提升AI生成代码的可靠性，但严格语法也加大了生成难度；现有编译器仅能在生成完成后给出反馈，约束解码方案需要白盒访问LLM且重实现语义约束成本极高，无法在生成过程中提前干预减少错误级联。
### 方法关键点
1. 提出生成式编译框架，核心是轻量语法引导的Sealor转换模块，可将生成过程中的不完整代码补全为标准编译器可诊断的完整程序，既不误判可补全的合法中间代码，又能保留足够上下文提前识别生成死路。
2. 基于类Rust演算实现Sealor并在Lean中完成性质证明，扩展为首个支持真实Rust的部分程序校验器。
### 关键结果
在仓库级Rust编码任务上测试黑盒/开源LLM，相比标准后生成反馈方案，非编译输出占比显著下降，功能正确性明显提升，可在错误发生早期检测到大量问题，有效减少错误级联。
