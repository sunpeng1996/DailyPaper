---
title: 'Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims
  in Small Language Models'
title_zh: 小语言模型工具使用能力低成本诊断框架：关键词匹配基准假阳性问题
authors:
- Juan S. Santillana
affiliations:
- Independent Researcher
- Globant
arxiv_id: '2610.02142'
url: https://arxiv.org/abs/2610.02142
pdf_url: https://arxiv.org/pdf/2610.02142
published: '2026-10-01'
collected: '2026-10-02'
category: Eval
direction: 小模型工具调用 · 评测诊断
tags:
- SmallLM
- ToolCalling
- Evaluation
- ModelDiagnosis
- SFT
one_liner: 揭露小模型工具使用评测的关键词匹配假阳性，提出低成本严格诊断阶梯
practical_value: '- 工具调用能力自动评测不要仅用关键词匹配，必须增加结构化校验（检查是否输出<|tool_call|>包裹的合法JSON），避免假阳性浪费迭代时间

  - 小模型工具调用能力缺失时，优先检测工具触发token的首token概率定位根因，不要盲目堆SFT数据：文中1B模型原6B token SFT无效，针对性调优后仅2202步就修复，成本降3个数量级

  - 训练小模型工具调用能力时，高占比代码预训练能让工具调用能力自发涌现，比事后堆web语料+SFT效率高得多

  - 验证模型原生能力时，优先用训练时的原生前向逻辑做greedy decode校验，避开推理服务层的格式丢失、token过滤等问题导致的误判'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有小语言模型工具使用能力的自动评测高度依赖关键词匹配基准，极易产生假阳性：将仅提及工具名的自由文本误判为合法工具调用，导致开发者误判模型能力，浪费大量SFT计算资源。
### 方法关键点
- 提出4层低成本诊断阶梯，全部仅需数分钟CPU时间：① 原有 lenient 关键词匹配基准；② 固定Prompt定性测试；③ 训练样本逐字复现校验+泛化测试（要求输出非完全照搬训练集的合法结构化工具调用）；④ 机制探针（工具触发token首token概率检测、embedding漂移校验）
- 采用架构、tokenizer、特殊token布局完全匹配的两个西班牙语安全小模型做自然对照：600M参数（预训练语料65%为代码技术文本，无专用工具SFT）、1B参数（预训练以web语料为主，配置了6B token专用工具SFT阶段）
- 针对1B模型的工具调用缺失问题，设计了混合语料（对话+工具语料+领域推理轨迹）、高学习率的轻量化SFT修复方案
### 关键结果
- 关键词匹配基准上两模型得分几乎一致（B4=0.660 vs 0.650），但严格诊断下600M 6/6输出合法泛化工具调用，1B 0/6完全不输出结构化调用
- 定位到1B的核心问题是<|tool_call|>触发token的首概率仅1e-4~1e-5，原6B token SFT完全未建立起触发先验
- 轻量化修复仅用2202步、3.3 GPU小时，就将1B的合法工具调用率从0.1提升到0.959，在238个未见实体Prompt上通过率达0.536，超过600M的0.428
> 最值得记住的结论：小模型特定能力的获取，语料构成的影响远大于参数量、训练token总数，盲目堆SFT数据不如先做精准诊断针对性调优
