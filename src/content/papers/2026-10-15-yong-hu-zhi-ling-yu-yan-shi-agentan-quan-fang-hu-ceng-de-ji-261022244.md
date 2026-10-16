---
title: Language Is a Security Surface for Agent Guards
title_zh: 用户指令语言是Agent安全防护层的攻击面
authors:
- Hasan Demirkiran
- Jens Ernstberger
affiliations:
- Kontext
arxiv_id: '2610.22244'
url: https://arxiv.org/abs/2610.22244
pdf_url: https://arxiv.org/pdf/2610.22244
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 安全防护层多语言鲁棒性评估
tags:
- Agent Safety
- Guardrail
- Multilingual Robustness
- LLM Security
- Benchmark
one_liner: 量化19款Agent step级防护层的多语言鲁棒性，证明用户指令语言是隐形安全攻击面
practical_value: '- 做多语言跨境电商导购/投放Agent的团队，不要用10B以下小模型做step级安全guard，这类模型在低资源语言下恶意请求漏过率最高可提升7.4pp，12~30B开源guard要注意优化多语言场景下的过拦截问题

  - 不要默认专用Agent guard的鲁棒性更强，其语言敏感性是所有guard类型中最高的，上线前必须做多语言场景专项测试，不能仅用英文benchmark验证

  - 多语言Guard的测试可优先选低资源语言+长枚举类多任务指令构造case，这类场景是故障高发区，能快速暴露稳定性问题

  - 单一语言场景业务可忽略该风险，多语言场景优先选用frontier大模型做guard，Gemini 3.8 Flash这类模型翻译前后裁决100%一致，无语言敏感性问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent的step级安全guard均基于英文数据训练、英文benchmark评估，但实际用户会使用任意语言发送请求，指令语言对guard裁决的影响从未被量化，是多语言Agent落地的隐形安全风险。
### 方法关键点
- 构建LINGUAGUARDBENCH：基于TS-Bench的1220条带标签工具调用步骤，仅翻译用户指令为德、法、土、斯瓦希里、阿姆哈拉5种覆盖高/中/低资源层级的语言，其余轨迹、工具调用、标签完全不变，确保裁决变化仅由语言差异导致
- 设置6种英文paraphrase、空白符安慰剂作为对照组，每个托管guard重复运行3次消除自身非确定性噪声
- 覆盖19款guard测试：包括frontier API、4B~30B开源通用模型、4款专用Agent guard（TS-Guard、ShieldAgent、Safiron、AgentDoG）
### 关键结果
- 13B参数以下的9款guard，平均安慰剂调整后的裁决翻转率从法语的1.5pp单调上升至阿姆哈拉语的4.4pp，语言越罕见波动越大
- 专用Agent guard的语言敏感性最高，斯瓦希里/阿姆哈拉语下平均翻转率达6.3pp
- 故障模式和模型规模强相关：12~30B开源guard多出现良性步骤过拦截（FPR最高提升5.0pp），10B以下guard多出现恶意请求漏过（TPR最高下降7.4pp）
- Frontier大模型几乎无波动，Gemini 3.8 Flash翻译前后裁决100%一致，仅靠轨迹即可完成安全判断，完全不依赖用户指令
### 核心结论
仅用英文数据训练和评估的Agent guard，其多语言场景下的故障不会在英文测试中暴露，语言本身就是一个未被重视的安全攻击面
