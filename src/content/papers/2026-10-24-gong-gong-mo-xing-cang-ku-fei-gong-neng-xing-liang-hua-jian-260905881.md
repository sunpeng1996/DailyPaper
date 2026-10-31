---
title: 'Broken on Arrival: Non-Functional Quantized LLM Artifacts in Public Model
  Registries and How to Catch Them'
title_zh: 公共模型仓库非功能性量化LLM工件的检测方法研究
authors:
- Aditi Patodiya
affiliations:
- Independent Researcher
arxiv_id: '2609.05881'
url: https://arxiv.org/abs/2609.05881
pdf_url: https://arxiv.org/pdf/2609.05881
published: '2026-10-24'
collected: '2026-10-31'
category: Eval
direction: LLM量化 · 功能有效性评测
tags:
- quantization
- GGUF
- LLM
- model-registry
- functional-testing
- calibration
one_liner: 测试327个公共仓库量化代码LLM，发现2.3%非功能性，推出30s快速筛查工具quantcheck
practical_value: '- 部署端侧轻量化LLM（如客服应答、Agent工具调用、推荐理由生成场景）时，不要直接使用公共仓库的Q2/Q3级低bit量化版本，必须先过15任务快速筛查，避免拿到完全失效的模型

  - 对3B-4B级小参数LLM做低bit量化时，必须加入importance matrix校准，Qwen2.5-Coder-3B实验显示校准可将代码生成能力从0提升至基准的46%-69%

  - 内部模型仓库上线量化模型版本时，可复用quantcheck的30s筛查流程作为准入门限，无需跑全量benchmark即可排除绝大多数非功能性版本，大幅降低测试成本

  - 下载第三方GGUF模型时，优先选择带imatrix/AWQ校准标识的版本，同时确认其chat template、预分词器配置与业务runtime匹配，避免配置不匹配导致的效果折损'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前本地部署LLM普遍直接从公共仓库下载GGUF格式量化模型，但主流公共仓库均未对量化版本做功能性测试，全球超32万公开自托管LLM服务可能用到完全失效的低bit量化版本，此前没有针对该问题的系统性规模化检测研究。
### 方法关键点
- 测试集覆盖305个Ollama官方代码能力LLM标签+22个Hugging Face热门社区GGUF文件，包含15个模型系列从Q2_K到fp16的全量化级别
- 设计15个简单代码任务的快速筛查用例，筛选得分≤2/15的疑似失效版本，再通过HumanEval+全164任务验证，将得分<10%的版本定义为非功能性
- 对疑似失效版本做配方对齐的重量化，通过tensor级对比区分失效原因是文件损坏、量化配方问题还是模型本身压缩极限
### 关键结果
- 2.3%的Ollama官方标签为非功能性版本，全部为≤4B参数模型的Q2_K到Q3_K_L低bit量化版本，部分版本HumanEval+得分为0
- 对Qwen2.5-Coder-3B失效版本加importance matrix校准后，3个量化级别的HumanEval+得分从0提升到76-113/164，达到基准的46-69%
- 15任务筛查单模型仅需30s生成时间，测试的66个通过筛查的标签无一非功能性，筛查准确率100%
### 核心结论
量化模型的可复现性不等于功能性，哪怕tensor完全对齐原始量化配方，未校准的低bit量化也可能完全失效，必须做功能性测试再上线
